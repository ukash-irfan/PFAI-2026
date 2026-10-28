import argparse
from pathlib import Path

import joblib
import pandas as pd
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

DEFAULT_BASE_PATH = r"C:\BSAI\3rd Semester\PROGRAMING FOR AI\LAB\week9"

FEATURES = ["temp_c", "vibration", "runtime", "pressure"]
TARGET = "fault"
REQUIRED = FEATURES + [TARGET]

RANDOM_STATE = 42
TEST_SIZE = 0.25
FINAL_MAX_DEPTH = 3
DEPTHS_TO_COMPARE = [1, 2, 3, 5, None]


def section(title):
    print(f"\n{'=' * 60}\n{title}\n{'=' * 60}")


def load_data(base_path):
    for folder in ("data", "models", "reports"):
        (base_path / folder).mkdir(parents=True, exist_ok=True)

    data_path = base_path / "data" / "machines_ml.csv"
    if not data_path.exists():
        raise FileNotFoundError(f"Dataset not found: {data_path}")
    return pd.read_csv(data_path)


def validate_data(machines):
    missing = set(REQUIRED) - set(machines.columns)
    if missing:
        raise ValueError(f"Missing columns: {sorted(missing)}")
    if machines[REQUIRED].isna().any().any():
        raise ValueError("Required columns contain missing values.")
    if not set(machines[TARGET].unique()).issubset({0, 1}):
        raise ValueError("fault must contain only 0 and 1.")
    if machines[TARGET].nunique() != 2:
        raise ValueError("Both Normal (0) and Fault (1) classes must be present.")
    print("All validation checks passed.")


def explore_data(machines):
    print(f"Rows: {machines.shape[0]}, Columns: {machines.shape[1]}")

    print("\nDescriptive statistics:")
    print(machines[REQUIRED].describe().round(2))

    print("\nClass counts (0=Normal; 1=Fault):")
    print(machines[TARGET].value_counts().sort_index())

    print("\nTarget class proportions:")
    proportions = (
        machines[TARGET]
        .value_counts(normalize=True)
        .sort_index()
        .mul(100)
        .rename(index={0: "Normal (0)", 1: "Fault (1)"})
        .rename("Proportion (%)")
        .round(2)
    )
    print(proportions)


def split_data(machines):
    X = machines[FEATURES]
    y = machines[TARGET]

    split_args = dict(test_size=TEST_SIZE, random_state=RANDOM_STATE, stratify=y)
    X_train, X_test, y_train, y_test = train_test_split(X, y, **split_args)

    print("Train:", X_train.shape, y_train.value_counts().to_dict())
    print("Test:", X_test.shape, y_test.value_counts().to_dict())

    distribution = pd.DataFrame({
        "Original count": y.value_counts().sort_index(),
        "Original %": y.value_counts(normalize=True).sort_index() * 100,
        "Training count": y_train.value_counts().sort_index(),
        "Training %": y_train.value_counts(normalize=True).sort_index() * 100,
        "Testing count": y_test.value_counts().sort_index(),
        "Testing %": y_test.value_counts(normalize=True).sort_index() * 100,
    })
    print("\nData Split Distribution:")
    print(distribution.round(2).to_string())

    X_train_again, X_test_again, _, _ = train_test_split(X, y, **split_args)
    assert X_train.equals(X_train_again) and X_test.equals(X_test_again)
    print(f"\nRepeated split with random_state={RANDOM_STATE} is identical.")

    return X_train, X_test, y_train, y_test


def train_and_evaluate(X_train, X_test, y_train, y_test):
    model = DecisionTreeClassifier(max_depth=FINAL_MAX_DEPTH, random_state=RANDOM_STATE)
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)

    cm = confusion_matrix(y_test, predictions)
    tn, fp, fn, tp = (int(v) for v in cm.ravel())

    manual_accuracy = (tn + tp) / cm.sum()
    assert abs(manual_accuracy - accuracy) < 1e-12

    # Accuracy of a model that always predicts the majority class.
    baseline = max(y_test.mean(), 1 - y_test.mean())

    print({"TN": tn, "FP": fp, "FN": fn, "TP": tp})
    print(f"Test Accuracy: {accuracy:.3f}  (always-Normal baseline: {baseline:.3f})")
    print("Manual accuracy verification successful!\n")
    print(classification_report(
        y_test, predictions, target_names=["Normal (0)", "Fault (1)"]
    ))

    return model, predictions


def compare_depths(X_train, X_test, y_train, y_test, reports_dir):
    results = []
    for depth in DEPTHS_TO_COMPARE:
        candidate = DecisionTreeClassifier(max_depth=depth, random_state=RANDOM_STATE)
        candidate.fit(X_train, y_train)

        train_score = candidate.score(X_train, y_train)
        test_score = candidate.score(X_test, y_test)
        results.append({
            "max_depth": str(depth),
            "train_accuracy": train_score,
            "test_accuracy": test_score,
            "gap": train_score - test_score,
        })

    comparison = pd.DataFrame(results)
    comparison_path = reports_dir / "model_comparison.csv"
    comparison.to_csv(comparison_path, index=False)

    print(comparison.round(3).to_string())
    print(f"\nModel comparison saved to: {comparison_path}")


def save_and_verify_model(model, X_test, test_predictions, models_dir):
    bundle_path = models_dir / "machine_predictor.joblib"
    joblib.dump({"model": model, "features": FEATURES}, bundle_path)

    loaded = joblib.load(bundle_path)
    reloaded_predictions = loaded["model"].predict(X_test[loaded["features"]])

    assert (reloaded_predictions == test_predictions).all()
    print(f"Model saved to: {bundle_path}")
    print("Model reloading verified successfully!")
    return loaded


def predict_new_machines(loaded):
    new_machines = pd.DataFrame([
        {"temp_c": 98, "vibration": 6.5, "runtime": 14200, "pressure": 3.2},
        {"temp_c": 61, "vibration": 1.2, "runtime": 2700, "pressure": 6.7},
        {"temp_c": 81, "vibration": 3.8, "runtime": 8600, "pressure": 4.8},
    ])

    feature_order = loaded["features"]
    if set(new_machines.columns) != set(feature_order):
        raise ValueError("Prediction columns do not match training features.")

    new_machines["predicted_fault"] = loaded["model"].predict(new_machines[feature_order])
    new_machines["status"] = new_machines["predicted_fault"].map({0: "Normal", 1: "Fault"})

    print(new_machines.to_string())


def main():
    parser = argparse.ArgumentParser(description="Machine fault prediction pipeline.")
    parser.add_argument(
        "--base-path",
        default=DEFAULT_BASE_PATH,
        help="Folder that contains data/machines_ml.csv "
             "(models/ and reports/ are created here).",
    )
    args = parser.parse_args()
    base_path = Path(args.base_path)

    section("1. Load and validate data")
    machines = load_data(base_path)
    validate_data(machines)

    section("2. Data exploration")
    explore_data(machines)

    section("3. Train/test split")
    X_train, X_test, y_train, y_test = split_data(machines)

    section("4. Train and evaluate Decision Tree")
    model, test_predictions = train_and_evaluate(X_train, X_test, y_train, y_test)

    section("5. Tree depth comparison")
    compare_depths(X_train, X_test, y_train, y_test, base_path / "reports")

    section("6. Save and reload model")
    loaded = save_and_verify_model(model, X_test, test_predictions, base_path / "models")

    section("7. Predictions for new machines")
    predict_new_machines(loaded)


if __name__ == "__main__":
    main()
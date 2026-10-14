import json
from pathlib import Path


class Experiment:
    def __init__(self, experiment_id, model_name, dataset_name, accuracy):
        if not 0 <= accuracy <= 1:
            raise ValueError("Accuracy must be between 0 and 1.")
        self.experiment_id = experiment_id
        self.model_name = model_name
        self.dataset_name = dataset_name
        self.accuracy = accuracy

    def to_dictionary(self):
        return {
            "experiment_id": self.experiment_id,
            "model_name": self.model_name,
            "dataset_name": self.dataset_name,
            "accuracy": self.accuracy,
        }

    @staticmethod
    def save_experiments(experiments, file_path):
        json_path = Path(file_path)
        json_path.parent.mkdir(parents=True, exist_ok=True)
        records = [experiment.to_dictionary() for experiment in experiments]

        with json_path.open("w", encoding="utf-8") as file:
            json.dump(records, file, indent=4)

    @staticmethod
    def load_experiments(file_path):
        json_path = Path(file_path)
        if not json_path.exists():
            return []
        try:
            with json_path.open("r", encoding="utf-8") as file:
                records = json.load(file)
        except json.JSONDecodeError:
            print("The experiment json data is invalid.")
            return []

        experiments = []
        for record in records:
            experiment = Experiment(
                record["experiment_id"],
                record["model_name"],
                record["dataset_name"],
                record["accuracy"],
            )
            experiments.append(experiment)

        return experiments


def add_experiment(experiments, experiment_id, model_name, dataset_name, accuracy):
    """Convert accuracy string/number, create Experiment instance, and append to list."""
    try:
        acc_float = float(accuracy)
    except ValueError, TypeError:
        raise ValueError(f"Accuracy value '{accuracy}' is non-numeric.")

    experiment = Experiment(experiment_id, model_name, dataset_name, acc_float)
    experiments.append(experiment)
    return experiment


def search_experiment(experiments, experiment_id):
    """Search for an experiment by its ID."""
    for exp in experiments:
        if exp.experiment_id == experiment_id:
            return exp
    return None


def find_best_experiment(experiments):
    """Find and return the experiment with the highest accuracy."""
    if not experiments:
        return None
    return max(experiments, key=lambda exp: exp.accuracy)


def run_assertions():
    """Execute required validation and assertion checks."""
    test_suite = []

    test_exp = add_experiment(test_suite, "TEST-1", "TestModel", "TestDataset", "0.75")
    assert test_exp.accuracy == 0.75, "String to float conversion failed."

    d = test_exp.to_dictionary()
    assert d["experiment_id"] == "TEST-1" and d["accuracy"] == 0.75, (
        "to_dictionary conversion failed."
    )

    assert search_experiment(test_suite, "TEST-1") is not None, (
        "Search existing experiment failed."
    )

    assert search_experiment(test_suite, "DOES_NOT_EXIST") is None, (
        "Search non-existent experiment failed."
    )

    add_experiment(test_suite, "TEST-2", "BetterModel", "TestDataset", 0.95)
    best = find_best_experiment(test_suite)
    assert best.experiment_id == "TEST-2", (
        "Selection of greatest accuracy experiment failed."
    )

    try:
        add_experiment(test_suite, "FAIL", "InvalidModel", "Dataset", 1.5)
        assert False, "Failed to raise ValueError for accuracy > 1."
    except ValueError:
        pass


def main():

    run_assertions()
    print("All assertion tests passed successfully.")

    lab_folder = Path(__file__).resolve().parent
    json_path = lab_folder / "data" / "experiments.json"

    experiments = []
    add_experiment(
        experiments, "EXP-001", "Logistic Regression", "Student Performance", 0.84
    )
    add_experiment(experiments, "EXP-002", "Decision Tree", "Student Performance", 0.88)
    add_experiment(
        experiments, "EXP-003", "K-Nearest Neighbours", "Student Performance", 0.91
    )

    Experiment.save_experiments(experiments, json_path)
    print("Experiments saved at:", json_path.resolve())

    reloaded = Experiment.load_experiments(json_path)
    print(f"Reloaded {len(reloaded)} experiments successfully.")


if __name__ == "__main__":
    main()

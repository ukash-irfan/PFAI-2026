import json
from pathlib import Path


class Experiment:
    """Represents an AI experiment with validated accuracy."""

    def __init__(self, experiment_id, model_name, dataset_name, accuracy):
        if not 0 <= accuracy <= 1:
            raise ValueError("Accuracy must be between 0 and 1.")
        self.experiment_id = experiment_id
        self.model_name = model_name
        self.dataset_name = dataset_name
        self.accuracy = accuracy

    def to_dictionary(self):
        """Convert the experiment object to a JSON-serializable dictionary."""
        return {
            "experiment_id": self.experiment_id,
            "model_name": self.model_name,
            "dataset_name": self.dataset_name,
            "accuracy": self.accuracy,
        }


    def save_experiments(experiments, file_path):
        json_path = Path(file_path)
        json_path.parent.mkdir(parents=True, exist_ok=True)
        experiment_records = []

        for experiment in experiments:
            experiment_records.append(experiment.to_dictionary())
        with json_path.open("w", encoding="utf-8") as file:
            json.dump(experiment_records, file, indent=4)


def main():
    lab_folder = Path(__file__).resolve().parent
    json_path = lab_folder / "data" / "experiments.json"
    experiments = [
        Experiment("EXP-001", "Logistic Regression", "Student Performance", 0.84),
        Experiment("EXP-002", "Decision Tree", "Student Performance", 0.88),
        Experiment("EXP-003", "K-Nearest Neighbours", "Student Performance", 0.91),
    ]

    save_experiments(experiments, json_path)
    print("Experiments saved at:", json_path.resolve())

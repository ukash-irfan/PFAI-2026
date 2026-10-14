class AIModel:
    """Base class for all AI models."""

    def __init__(self, model_name):
        self.model_name = model_name
        self.is_trained = False

    def train(self):
        """Simulate model training state."""
        self.is_trained = True

    def describe(self):
        """Return generic model description."""
        return f"Model: {self.model_name}"


class ClassificationModel(AIModel):
    """This subclass is a relationship with AI Modelthat representing categorical prediction."""

    def __init__(self, model_name, classes):
        super().__init__(model_name)
        self.classes = classes

    def describe(self):
        """Override describe to include target classes."""
        return f"{super().describe()} | Classes: {self.classes}"


class RegressionModel(AIModel):
    """This Subclass ia a relationship that representing continuous prediction models."""

    def __init__(self, model_name, target_name):
        super().__init__(model_name)
        self.target_name = target_name

    def describe(self):
        """Override describe to include continuous target name."""
        return f"{super().describe()} | Target: {self.target_name}"


def main():
    """Create models, run training, and display profiles."""
    clf = ClassificationModel("Random Forest", ["Cat", "Dog"])
    reg = RegressionModel("Linear Regression", "House Price")

    clf.train()
    reg.train()

    print(f"{clf.describe()} | Trained: {clf.is_trained}")
    print(f"{reg.describe()} | Trained: {reg.is_trained}")


if __name__ == "__main__":
    main()

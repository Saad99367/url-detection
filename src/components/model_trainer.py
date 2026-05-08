import sys

from sklearn.ensemble import RandomForestClassifier

from src.config.config import (
    ModelTrainerConfig
)

from src.utils.logger import logging
from src.utils.exception import UrlException

from src.utils.utils import (
    save_object,
    classification_metrics
)


class ModelTrainer:
    """
    Model Trainer Component
    """

    def __init__(self):

        self.config = ModelTrainerConfig()

    def initiate_model_trainer(
        self,
        X_train,
        X_test,
        y_train,
        y_test
    ):
        """
        Train Random Forest model
        """

        try:

            logging.info(
                "Model training started"
            )

            # Model
            model = RandomForestClassifier(
                n_estimators=200,
                n_jobs=-1, 
                random_state=42
            )

            logging.info(
                "Random Forest model initialized"
            )

            # Train model
            model.fit(
                X_train,
                y_train
            )

            logging.info(
                "Model training completed"
            )

            # Prediction
            y_pred = model.predict(
                X_test
            )

            logging.info(
                "Prediction completed"
            )

            # Metrics
            accuracy, report = classification_metrics(y_test, y_pred) 

            print("\n")
            print("=" * 100)

            print("Random Forest Results")

            print(f"\nAccuracy: {accuracy:.4f}")

            print("\nClassification Report:\n")

            print(report)

            print("=" * 100)

            logging.info(
                f"Model Accuracy: {accuracy}"
            )

            # Save model
            save_object(
                self.config.trained_model_path,
                model
            )

            logging.info(
                "Model saved successfully"
            )

            return accuracy

        except Exception as e:

            raise UrlException(e, sys)


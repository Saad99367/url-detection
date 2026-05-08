from src.components.data_ingestion import (
    DataIngestion
)

from src.components.data_transformation import (
    DataTransformation
)

from src.components.model_trainer import (
    ModelTrainer
)

from src.utils.logger import logging
from src.utils.exception import UrlException

import sys


class TrainingPipeline:
    """
    Complete Training Pipeline
    """

    def __init__(self):

        pass

    def start_training_pipeline(self):

        try:

            logging.info(
                "Training pipeline started"
            )

            # =========================
            # Data Ingestion
            # =========================

            ingestion = DataIngestion()

            raw_path, train_path, test_path = (
                ingestion.init_data_ingestion()
            )

            logging.info(
                "Data ingestion completed"
            )

            # =========================
            # Data Transformation
            # =========================

            transformation = DataTransformation()

            X_train, X_test, y_train, y_test = (
                transformation.data_transformation(
                    train_path=train_path,
                    test_path=test_path
                )
            )

            logging.info(
                "Data transformation completed"
            )

            # =========================
            # Model Training
            # =========================

            trainer = ModelTrainer()

            accuracy = (
                trainer.initiate_model_trainer(
                    X_train,
                    X_test,
                    y_train,
                    y_test
                )
            )

            logging.info(
                "Model training completed"
            )

            print("\n")
            print("=" * 100)

            print(
                f"Training Pipeline Finished Successfully"
            )

            print(
                f"\nFinal Accuracy: {accuracy:.4f}"
            )

            print("=" * 100)

        except Exception as e:

            raise UrlException(e, sys)


if __name__ == "__main__":

    pipeline = TrainingPipeline()

    pipeline.start_training_pipeline()
import sys
import re

import pandas as pd

from sklearn.feature_extraction.text import (
    TfidfVectorizer
)

from src.config.constants import (
    TEXT_COLUMN,
    TARGET_COLUMN
)

from src.config.config import (
    DataTransformationConfig
)

from src.utils.logger import logging
from src.utils.exception import UrlException
from src.utils.utils import save_object


class DataTransformation:
    """
    Data Transformation Component
    """

    def __init__(self):

        self.config = DataTransformationConfig()

    @staticmethod
    def clean_url(url: str):
        """
        Clean URL text
        """

        url = str(url).lower()

        # Remove extra spaces
        url = url.strip()

        # Remove www
        url = re.sub(
            r"www\.",
            "",
            url
        )

        return url

    def data_transformation(
        self,
        train_path,
        test_path
    ):

        try:

            logging.info(
                "Data transformation started..."
            )

            # Load datasets
            train_data = pd.read_csv(
                train_path
            )

            test_data = pd.read_csv(
                test_path
            )

            logging.info(
                "Train/Test data loaded successfully"
            )

            # Input features
            X_train = train_data[
                TEXT_COLUMN
            ]

            X_test = test_data[
                TEXT_COLUMN
            ]

            # Target features
            y_train = train_data[
                TARGET_COLUMN
            ]

            y_test = test_data[
                TARGET_COLUMN
            ]

            logging.info(
                "Input and target features separated"
            )

            # Clean URLs
            X_train = X_train.apply(
                self.clean_url
            )

            X_test = X_test.apply(
                self.clean_url
            )

            logging.info(
                "URL cleaning completed"
            )

            # TF-IDF
            tfidf = TfidfVectorizer(
                analyzer='char',
                ngram_range=(3, 5)
            )

            # Fit and transform training data
            X_train = tfidf.fit_transform(
                X_train
            )

            # Transform test data
            X_test = tfidf.transform(
                X_test
            )

            logging.info(
                "TF-IDF transformation completed"
            )

            # Debugging
            print(
                f"TF-IDF Features: "
                f"{len(tfidf.vocabulary_)}"
            )

            print(
                f"X_train Shape: "
                f"{X_train.shape}"
            )

            print(
                f"X_test Shape: "
                f"{X_test.shape}"
            )

            # Save TF-IDF object
            save_object(
                self.config.tfidf_path,
                tfidf
            )

            logging.info(
                "TF-IDF object saved successfully"
            )

            return (
                X_train,
                X_test,
                y_train,
                y_test
            )

        except Exception as e:

            logging.error(
                f"Error in data transformation: {e}"
            )

            raise UrlException(e, sys)
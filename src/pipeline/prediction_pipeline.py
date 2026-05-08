import sys

from src.config.constants import (
    MODEL_FILE_PATH,
    TFIDF_FILE_PATH
)

from src.utils.logger import logging
from src.utils.exception import UrlException

from src.utils.utils import load_object


class PredictionPipeline:
    """
    Prediction Pipeline
    """

    def __init__(self):

        self.model_path = MODEL_FILE_PATH
        self.tfidf_path = TFIDF_FILE_PATH

        # Load model and TF-IDF once
        self.model = load_object(
            self.model_path
        )

        self.tfidf = load_object(
            self.tfidf_path
        )

        logging.info(
            "Model and TF-IDF loaded successfully"
        )

    def predict(self, url: str):

        try:

            logging.info(
                "Prediction pipeline started"
            )

            # Transform URL
            transformed_url = self.tfidf.transform(
                [url]
            )

            logging.info(
                "URL transformed successfully"
            )

            # Prediction
            prediction = self.model.predict(
                transformed_url
            )[0]

            # Prediction probabilities
            probability = self.model.predict_proba(
                transformed_url
            )[0]

            # Confidence score
            confidence = round(
                max(probability) * 100,
                2
            )

            # Debugging
            print("\n")
            print("=" * 50)
            print(f"URL: {url}")
            print(f"Raw Prediction: {prediction}")
            print(f"Probabilities: {probability}")
            print("=" * 50)

            # Correct label mapping
            # 0 -> Legitimate
            # 1 -> Phishing

            if prediction == 0:
                label = "Legitimate"
            else:
                label = "Phishing"

            logging.info(
                f"Prediction completed: {label}"
            )

            return {
                "Prediction": label,
                "Confidence": f"{confidence:.2f}%"
            }

        except Exception as e:

            logging.error(
                f"Prediction error: {e}"
            )

            raise UrlException(e, sys)


if __name__ == "__main__":

    pipeline = PredictionPipeline()

    urls = [
        "https://www.microsoft.com",
        "https://www.google.com",
        "https://github.com",
        "http://paypal-login-security-update.com",
        "http://verify-account-freegift.xyz",
        "http://192.168.1.1/login",
        "https://secure-bank-login-update.xyz"
    ]

    print("\n" + "=" * 100)
    print("PHISHING URL DETECTION RESULTS")
    print("=" * 100)

    for url in urls:

        result = pipeline.predict(url)

        print(f"\nURL: {url}")
        print(f"Prediction : {result['Prediction']}")
        print(f"Confidence : {result['Confidence']}")

        print("-" * 100)

    print("=" * 100)
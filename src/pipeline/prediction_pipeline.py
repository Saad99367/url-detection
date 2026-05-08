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

        try:

            self.model_path = MODEL_FILE_PATH
            self.tfidf_path = TFIDF_FILE_PATH

            # Load model
            self.model = load_object(
                self.model_path
            )

            # Load TF-IDF
            self.tfidf = load_object(
                self.tfidf_path
            )

            logging.info(
                "Model and TF-IDF loaded successfully"
            )

        except Exception as e:

            raise UrlException(e, sys)

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

            # Default probabilities
            legit_prob = 0
            phishing_prob = 0

            # Check if model supports probabilities
            if hasattr(self.model, "predict_proba"):

                probabilities = self.model.predict_proba(
                    transformed_url
                )[0]

                legit_prob = round(
                    probabilities[0] * 100,
                    2
                )

                phishing_prob = round(
                    probabilities[1] * 100,
                    2
                )

            # Convert prediction to label
            if prediction == 0:
                label = "✅ Legitimate"
            else:
                label = "⚠️ Phishing"

            logging.info(
                f"Prediction completed: {label}"
            )

            # Debugging
            print("\n" + "=" * 50)
            print(f"URL: {url}")
            print(f"Prediction: {label}")
            print(f"Legitimate Probability: {legit_prob}%")
            print(f"Phishing Probability: {phishing_prob}%")
            print("=" * 50)

            return {

                "Prediction": label,

                "Legitimate Probability":
                    f"{legit_prob}%",

                "Phishing Probability":
                    f"{phishing_prob}%"
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

        print(
            f"Prediction : "
            f"{result['Prediction']}"
        )

        print(
            f"Legitimate : "
            f"{result['Legitimate Probability']}"
        )

        print(
            f"Phishing : "
            f"{result['Phishing Probability']}"
        )

        print("-" * 100)

    print("=" * 100)
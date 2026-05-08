import streamlit as st

from src.pipeline.prediction_pipeline import PredictionPipeline


# Page Config
st.set_page_config(

    page_title="URL Phishing Detection",

    page_icon="🔍",

    layout="centered"
)


# Load Pipeline
pipeline = PredictionPipeline()


# Title
st.title("🔍 URL Phishing Detection")

st.markdown(
    """
    Detect phishing websites using Machine Learning + TF-IDF
    """
)


# Input
url = st.text_input(

    "Enter URL",

    placeholder="https://example.com"
)


# Predict
if st.button("Predict"):

    if url.strip() == "":

        st.warning(
            "Please enter a URL"
        )

    else:

        result = pipeline.predict(url)

        prediction = result["Prediction"]

        legit = result["Legitimate Probability"]

        phishing = result["Phishing Probability"]


        # Show Prediction
        if "Phishing" in prediction:

            st.error(prediction)

        else:

            st.success(prediction)


        # Probabilities
        st.subheader(
            "Prediction Probabilities"
        )

        st.write(
            f"✅ Legitimate : {legit}"
        )

        st.write(
            f"⚠️ Phishing : {phishing}"
        )
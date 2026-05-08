import gradio as gr

from src.pipeline.prediction_pipeline import PredictionPipeline


# Load pipeline
pipeline = PredictionPipeline()


def predict_url(url):

    result = pipeline.predict(url)

    return {

        "Prediction":
            result["Prediction"],

        "Legitimate":
            result["Legitimate Probability"],

        "Phishing":
            result["Phishing Probability"]
    }


# Gradio Interface
interface = gr.Interface(

    fn=predict_url,

    inputs=gr.Textbox(
        lines=2,
        placeholder="Enter URL here...",
        label="URL"
    ),

    outputs=gr.JSON(
        label="Prediction Result"
    ),

    title="🔍 URL Phishing Detection",

    description="""
    Detect phishing websites using Machine Learning + TF-IDF
    """,

    theme=gr.themes.Soft()
)


# Launch
if __name__ == "__main__":

    interface.launch()
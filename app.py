from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from src.pipeline.prediction_pipeline import (
    PredictionPipeline
)

app = FastAPI()


# Static Files
app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)


# Templates
templates = Jinja2Templates(
    directory="templates"
)


@app.get("/", response_class=HTMLResponse)
def home(request: Request):

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request
        }
    )


@app.post("/predict", response_class=HTMLResponse)
def predict(
    request: Request,
    url: str = Form(...)
):

    pipeline = PredictionPipeline()

    result = pipeline.predict(url)

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "prediction": result["Prediction"],
            "confidence": result["Confidence"],
            "url": url
        }
    )
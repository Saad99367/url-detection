from dataclasses import dataclass

from src.config.constants import (
    DATA_FILE_PATH,
    TARGET_COLUMN,
    TEXT_COLUMN,
    MODEL_FILE_PATH,
    TFIDF_FILE_PATH
)


# =========================
# Data Ingestion Config
# =========================

@dataclass
class DataIngestionConfig:

    data_path: str = DATA_FILE_PATH


# =========================
# Data Transformation Config
# =========================

@dataclass
class DataTransformationConfig:

    text_column: str = TEXT_COLUMN

    target_column: str = TARGET_COLUMN

    tfidf_path: str = TFIDF_FILE_PATH


# =========================
# Model Trainer Config
# =========================

@dataclass
class ModelTrainerConfig:

    trained_model_path: str = MODEL_FILE_PATH
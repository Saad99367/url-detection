import os


# =========================
# Project Directories
# =========================

ARTIFACTS_DIR: str = "artifacts/data"

DATA_DIR: str = "data"

MODELS_DIR: str = os.path.join(
    ARTIFACTS_DIR,
    "models"
)


# =========================
# Dataset Information
# =========================

DATA_FILE_NAME: str = "raw.csv"

TARGET_COLUMN: str = "label"

TEXT_COLUMN: str = "url"


# =========================
# Dataset Paths
# =========================

DATA_FILE_PATH: str = os.path.join(
    DATA_DIR,
    DATA_FILE_NAME
)


# =========================
# Saved Model Files
# =========================

MODEL_FILE_NAME: str = "model.pkl"

TFIDF_FILE_NAME: str = "tfidf.pkl"


# =========================
# Saved Paths
# =========================

MODEL_FILE_PATH: str = os.path.join(
    MODELS_DIR,
    MODEL_FILE_NAME
)

TFIDF_FILE_PATH: str = os.path.join(
    MODELS_DIR,
    TFIDF_FILE_NAME
)
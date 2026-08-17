import joblib
from pathlib import Path


BASE_DIR = Path(__file__).parent


class RiskEngine:

    def __init__(self):

        self.model = joblib.load(
            BASE_DIR / "risk_model.pkl"
        )

        self.label_encoders = joblib.load(
            BASE_DIR / "label_encoders.pkl"
        )

        self.feature_columns = joblib.load(
            BASE_DIR / "feature_columns.pkl"
        )
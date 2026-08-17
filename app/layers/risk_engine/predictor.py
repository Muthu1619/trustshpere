import joblib
import pandas as pd
from pathlib import Path

from app.layers.risk_engine.models import RiskAssessment
BASE_DIR = Path(__file__).parent


class RiskPredictor:

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
    

    def predict(self, proposal,reputation):

        transaction_time = proposal.transaction_time

        data = {
            "amount": proposal.amount,
            "category": proposal.category,
            "merchant": proposal.merchant,
            "reputation": reputation,
            "hour": transaction_time.hour,
            "day_of_week": transaction_time.weekday(),
            "month": transaction_time.month,
            "is_weekend": int(
                transaction_time.weekday() >= 5
            )
        }

        df = pd.DataFrame([data])

        for col, encoder in self.label_encoders.items():

            if col != "risk_level":
                df[col] = encoder.transform(df[col])

        df = df[self.feature_columns]

        prediction = self.model.predict(df)[0]

        probabilities = self.model.predict_proba(df)[0]

        risk_score = float(max(probabilities))

        prediction = self.label_encoders[
            "risk_level"
        ].inverse_transform([prediction])[0]

        return RiskAssessment(
    risk_level=prediction,
    risk_score=risk_score
)
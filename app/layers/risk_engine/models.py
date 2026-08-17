from pydantic import BaseModel


class RiskAssessment(BaseModel):
    risk_level: str
    risk_score: float
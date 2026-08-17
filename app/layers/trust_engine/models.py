from pydantic import BaseModel


class TrustResult(BaseModel):

    trust_score: float
    decision: str
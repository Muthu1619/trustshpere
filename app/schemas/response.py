from pydantic import BaseModel


class EvaluateResponse(BaseModel):
    intent: str

    category: str

    estimated_amount: float

    currency: str

    confidence: float

    confidence_reason: str

    requires_payment: bool

    reasoning: str

    reputation: str
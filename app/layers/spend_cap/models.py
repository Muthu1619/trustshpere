from pydantic import BaseModel


class SpendCapResult(BaseModel):
    within_cap: bool
    transaction_amount: float
    max_amount: float
    reason: str
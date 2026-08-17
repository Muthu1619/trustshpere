from pydantic import BaseModel
from datetime import datetime

class TransactionProposal(BaseModel):
    action: str
    category: str
    merchant: str
    amount: float
    currency: str
    transaction_time: datetime
    raw_prompt: str
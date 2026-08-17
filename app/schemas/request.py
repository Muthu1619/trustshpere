from pydantic import BaseModel


class EvaluateRequest(BaseModel):
    agent: str
    prompt: str
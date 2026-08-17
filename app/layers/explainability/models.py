from pydantic import BaseModel


class ExplainabilityResult(BaseModel):

    summary: str
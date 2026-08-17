import json

from app.schemas.response import EvaluateResponse


def parse_llm_response(response: str) -> EvaluateResponse:

    data = json.loads(response)

    return EvaluateResponse(**data)
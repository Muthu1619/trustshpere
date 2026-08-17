from typing import Any, Optional

from pydantic import BaseModel

from app.schemas.proposal import TransactionProposal
from app.schemas.response import EvaluateResponse
from app.layers.spend_cap.models import SpendCapResult
from app.layers.risk_engine.models import RiskAssessment
from app.layers.trust_engine.models import TrustResult
from app.layers.explainability.models import ExplainabilityResult

class PipelineContext(BaseModel):

    proposal: TransactionProposal

    intent_analysis: Optional[EvaluateResponse] = None

    spend_cap: Optional[SpendCapResult] = None

    risk_assessment: Optional[RiskAssessment] = None

    trust: Optional[TrustResult] = None

    explanation: Optional[ExplainabilityResult] = None


    final_decision: Optional[dict] = None
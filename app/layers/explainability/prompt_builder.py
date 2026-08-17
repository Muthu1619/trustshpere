import json

from app.layers.explainability.prompts import (
    EXPLAINABILITY_PROMPT
)


class ExplainabilityPromptBuilder:

    @staticmethod
    def build(context) -> str:

        payload = {

            "proposal":
                context.proposal.model_dump(),

            "intent_analysis":
                context.intent_analysis.model_dump(),

            "spend_cap":
                context.spend_cap.model_dump(),

            "risk_assessment":
                context.risk_assessment.model_dump(),

            "trust":
                context.trust.model_dump()

        }

        return f"""
{EXPLAINABILITY_PROMPT}

Pipeline Context:

{json.dumps(payload, indent=2, default=str)}
"""
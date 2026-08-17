import json
from pathlib import Path


class AuditStorage:

    FILE_PATH = Path(__file__).parent / "audit_logs.json"

    @classmethod
    def save(cls, context):

        transaction = {

            "proposal": context.proposal.model_dump(),

            "intent_analysis": context.intent_analysis.model_dump(),

            "spend_cap": context.spend_cap.model_dump(),

            "risk_assessment": context.risk_assessment.model_dump(),

            "trust": context.trust.model_dump(),

            "explanation": (
                context.explanation.model_dump()
                if context.explanation
                else None
            )
        }

        logs = []

        if cls.FILE_PATH.exists():

            with open(cls.FILE_PATH, "r") as f:

                logs = json.load(f)

        logs.append(transaction)

        with open(cls.FILE_PATH, "w") as f:

            json.dump(
                logs,
                f,
                indent=4,
                default=str
            )
import json

from app.layers.intent_analyzer.prompts import INTENT_ANALYZER_PROMPT
from app.schemas.proposal import TransactionProposal


class IntentPromptBuilder:

    @staticmethod
    def build(proposal: TransactionProposal) -> str:
        return f"""
{INTENT_ANALYZER_PROMPT}

Transaction Proposal:

{json.dumps(proposal.model_dump(), indent=2,default =str)}
"""
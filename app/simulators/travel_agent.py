from app.schemas.proposal import TransactionProposal
from app.simulators.base_agent import BaseAgentSimulator
from datetime import datetime

class TravelAgentSimulator(BaseAgentSimulator):

    def create_proposal(self, prompt: str) -> TransactionProposal:

        return TransactionProposal(
            action="book_flight",
            category="Travel",
            merchant="charter",
            amount=2000,
            currency="INR",
            transaction_time=datetime(2026, 7, 23, 23, 45),
            raw_prompt=prompt
        )
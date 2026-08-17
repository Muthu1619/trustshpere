from abc import ABC, abstractmethod
from app.schemas.proposal import TransactionProposal


class BaseAgentSimulator(ABC):

    @abstractmethod
    def create_proposal(self, prompt: str) -> TransactionProposal:
        pass
from app.core.governance_pipeline import GovernancePipeline
from app.schemas.proposal import TransactionProposal
from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/gateway",
    tags=["Gateway"]
)


@router.post("/evaluate")
def evaluate(proposal: TransactionProposal):

    try:

        pipeline = GovernancePipeline()

        context = pipeline.execute(proposal)

        return context

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
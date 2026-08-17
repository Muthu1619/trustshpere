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

    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
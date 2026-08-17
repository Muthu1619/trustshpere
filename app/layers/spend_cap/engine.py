from app.layers.spend_cap.models import SpendCapResult
from app.layers.spend_cap.policies import SPENDING_POLICIES


class SpendCapManager:

    def evaluate(self, category: str, amount: float) -> SpendCapResult:

        max_amount = SPENDING_POLICIES.get(category, {}).get("max_amount")

        if max_amount is None:
            return SpendCapResult(
                within_cap=False,
                transaction_amount=amount,
                max_amount=0,
                reason=f"No spending policy found for category '{category}'."
            )

        if amount <= max_amount:
            return SpendCapResult(
                within_cap=True,
                transaction_amount=amount,
                max_amount=max_amount,
                reason="Transaction is within the configured spending limit."
            )

        return SpendCapResult(
            within_cap=False,
            transaction_amount=amount,
            max_amount=max_amount,
            reason=f"Transaction exceeds the spending limit by ${amount - max_amount:.2f}."
        )
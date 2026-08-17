from app.layers.trust_engine.models import TrustResult


class TrustEngine:

    def evaluate(
        self,
        confidence,
        risk_score,
        risk_level,
        within_cap
    ):

        spend_score = int(within_cap)

        trust_score = (
            0.5 * confidence
            + 0.3 * (1 - risk_score)
            + 0.2 * spend_score
        )

        if risk_level == "High":
            decision = "REVIEW"

        elif trust_score < 0.6:
            decision = "REVIEW"
        else:
            decision = "APPROVE"

        return TrustResult(
            trust_score=round(trust_score, 2),
            decision=decision
        )
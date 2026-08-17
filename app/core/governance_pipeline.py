from app.layers.intent_analyzer.analyzer import IntentAnalyzer
from app.schemas.pipeline import PipelineContext
from app.layers.spend_cap.engine import SpendCapManager
from app.layers.risk_engine.predictor import RiskPredictor
from app.layers.trust_engine.engine import TrustEngine
from app.layers.explainability.engine import ExplainabilityEngine
from app.layers.audit.storage import AuditStorage
class GovernancePipeline:

    def __init__(self):
        
        self.intent_analyzer = IntentAnalyzer()
        self.trust_engine = TrustEngine()
        self.risk_predictor = RiskPredictor()
        self.spend_cap_manager = SpendCapManager()
        self.explainability_engine = ExplainabilityEngine()
    def execute(self, proposal):

        context = PipelineContext(
            proposal=proposal
        )

        context.intent_analysis = self.intent_analyzer.analyze(
            context.proposal
        )
        context.spend_cap = self.spend_cap_manager.evaluate(
            category=context.proposal.category,
            amount=context.proposal.amount
        )

        context.risk_assessment = self.risk_predictor.predict(context.proposal, context.intent_analysis.reputation)

        context.trust = (
            self.trust_engine.evaluate(
                confidence=context.intent_analysis.confidence,
                risk_score=context.risk_assessment.risk_score,
                risk_level=context.risk_assessment.risk_level,
                within_cap=context.spend_cap.within_cap
            )
        )

        context.explanation = self.explainability_engine.generate(context)

        context.final_decision = {
            "trust": context.trust.model_dump(),
            "explanation": (
                context.explanation.model_dump()
                if context.explanation
                else None
            )
        }

        AuditStorage.save(context)
        return context
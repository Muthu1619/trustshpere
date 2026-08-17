from app.integrations.llm.gemini_client import GeminiClient

from app.layers.explainability.prompt_builder import (
    ExplainabilityPromptBuilder
)

from app.layers.explainability.models import (
    ExplainabilityResult
)


class ExplainabilityEngine:

    def __init__(self):

        self.gemini = GeminiClient()

    def generate(self, context):

        if context.trust.decision != "REVIEW":

            return None

        prompt = ExplainabilityPromptBuilder.build(
            context
        )

        response = self.gemini.generate(
            prompt
        )

        return ExplainabilityResult(
            summary=response
        )
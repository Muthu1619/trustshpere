import json

from app.integrations.llm.gemini_client import GeminiClient
from app.layers.intent_analyzer.prompts import INTENT_ANALYZER_PROMPT
from app.schemas.response import EvaluateResponse
from app.layers.intent_analyzer.parser import parse_llm_response
from app.layers.intent_analyzer.prompt_builder import IntentPromptBuilder
class IntentAnalyzer:

    def __init__(self):
        self.llm = GeminiClient()

    def analyze(self, proposal):

        prompt = IntentPromptBuilder.build(proposal)

        response = self.llm.generate(prompt)

        return parse_llm_response(response)
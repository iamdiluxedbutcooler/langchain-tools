from langchain.tools import BaseTool

class QuestionTypeClassifierTool(BaseTool):
    name = "question_type_classifier"
    description = "Classifies questions into types: factual, causal, comparison, calculation, etc."

    def _run(self, text: str) -> str:
        return self.classify(text)

    def _arun(self, text: str) -> str:
        raise NotImplementedError("QuestionTypeClassifierTool does not support async.")

    @staticmethod
    def classify(text: str) -> str:
        lower = text.lower()
        if any(word in lower for word in ["how come", "why"]):
            return "causal"
        if any(word in lower for word in ["who", "when", "where", "what"]):
            return "factual"
        if any(word in lower for word in ["compare", "difference", "versus"]):
            return "comparison"
        if any(char in lower for char in "+-*/="):
            return "calculation"
        if lower.endswith("?"):
            return "general_question"
        return "unknown"

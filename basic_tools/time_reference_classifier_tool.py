from langchain.tools import BaseTool
import re

class TimeReferenceClassifierTool(BaseTool):
    name = "time_reference_classifier"
    description = "Classifies whether the input refers to past, present, future, or is timeless."

    def _run(self, text: str) -> str:
        return self.classify(text)

    def _arun(self, text: str) -> str:
        raise NotImplementedError("TimeReferenceClassifierTool does not support async.")

    @staticmethod
    def classify(text: str) -> str:
        t = text.lower()
        if re.search(r"\b(was|had|did|before|yesterday|ago)\b", t):
            return "past"
        if re.search(r"\b(is|am|are|now|today|currently)\b", t):
            return "present"
        if re.search(r"\b(will|shall|going to|tomorrow|soon|next)\b", t):
            return "future"
        return "timeless"

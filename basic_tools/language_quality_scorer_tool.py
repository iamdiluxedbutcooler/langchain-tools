from langchain.tools import BaseTool
from textblob import TextBlob

class LanguageQualityScorerTool(BaseTool):
    name = "language_quality_scorer"
    description = "Estimates the English writing quality score (0-100) for a given text."

    def _run(self, text: str) -> int:
        return self.score_quality(text)

    def _arun(self, text: str) -> int:
        raise NotImplementedError("LanguageQualityScorerTool does not support async.")

    @staticmethod
    def score_quality(text: str) -> int:
        if not isinstance(text, str):
            raise ValueError("Input must be a string.")

        blob = TextBlob(text)
        mistakes = len(blob.correct().split()) - len(blob.words)
        words = len(blob.words)

        if words == 0:
            return 0

        error_rate = mistakes / words
        score = max(0, int(100 * (1 - error_rate)))
        return score

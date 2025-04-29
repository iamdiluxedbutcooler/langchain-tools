from langchain.tools import BaseTool
from textblob import TextBlob

class EmotionClassifierTool(BaseTool):
    name = "emotion_classifier"
    description = "Classify the dominant emotion (happy, sad, angry, neutral) from a given text."

    def _run(self, text: str) -> str:
        return self.classify_emotion(text)

    def _arun(self, text: str) -> str:
        raise NotImplementedError("EmotionClassifierTool does not support async.")

    @staticmethod
    def classify_emotion(text: str) -> str:
        if not isinstance(text, str):
            raise ValueError("Input must be a string.")

        polarity = TextBlob(text).sentiment.polarity

        if polarity > 0.5:
            return "happy"
        elif polarity < -0.5:
            return "angry"
        elif -0.5 <= polarity <= 0.5 and polarity != 0:
            return "sad"
        else:
            return "neutral"

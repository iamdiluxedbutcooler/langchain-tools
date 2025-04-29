from langchain.tools import BaseTool

class IntentRecognizerTool(BaseTool):
    name = "intent_recognizer"
    description = "Recognize the user's probable intent behind a text (ask, request, complain, confirm, other)."

    def _run(self, text: str) -> str:
        return self.recognize_intent(text)

    def _arun(self, text: str) -> str:
        raise NotImplementedError("IntentRecognizerTool does not support async.")

    @staticmethod
    def recognize_intent(text: str) -> str:
        text = text.lower()

        if any(word in text for word in ["can you", "could you", "please", "would you"]):
            return "request"
        elif text.endswith("?"):
            return "ask"
        elif any(word in text for word in ["not working", "problem", "issue", "hate"]):
            return "complain"
        elif any(word in text for word in ["sure", "okay", "alright", "yes", "confirmed"]):
            return "confirm"
        else:
            return "other"

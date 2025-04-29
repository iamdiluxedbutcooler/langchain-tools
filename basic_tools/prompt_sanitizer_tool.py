from langchain.tools import BaseTool
import re

class PromptSanitizerTool(BaseTool):
    name = "prompt_sanitizer"
    description = "Strips potential LLM prompt injection phrases and known jailbreak tricks."

    def _run(self, text: str) -> str:
        return self.sanitize(text)

    def _arun(self, text: str) -> str:
        raise NotImplementedError("PromptSanitizerTool does not support async.")

    @staticmethod
    def sanitize(text: str) -> str:
        dangerous_patterns = [
            r"(ignore\s+previous\s+instructions)",
            r"(you\s+are\s+now\s+a\s+.+?assistant)",
            r"(repeat\s+after\s+me)",
            r"(pretend\s+to\s+be)",
            r"(act\s+as\s+an?)",
            r"(as\s+an\s+AI\s+language\s+model)",
            r"(forget\s+everything\s+before)"
        ]
        for pattern in dangerous_patterns:
            text = re.sub(pattern, "[REMOVED]", text, flags=re.IGNORECASE)
        return text.strip()

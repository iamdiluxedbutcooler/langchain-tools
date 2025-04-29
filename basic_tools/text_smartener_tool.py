from langchain.tools import BaseTool
from textblob import TextBlob
import unicodedata
import re

class TextSmartenerTool(BaseTool):
    name = "text_smartener"
    description = (
        "Automatically clean, correct spelling, and normalize text input. "
        "Useful for pre-processing noisy user input before using a language model."
    )

    def _run(self, text: str) -> str:
        """
        Run the text smartener.
        """
        return self.smarten(text)

    def _arun(self, text: str) -> str:
        """
        Asynchronous version not implemented.
        """
        raise NotImplementedError("TextSmartenerTool does not support async.")

    @staticmethod
    def smarten(text: str) -> str:
        if not isinstance(text, str):
            raise ValueError("Input must be a string.")
        
        # Correct spelling
        corrected_text = str(TextBlob(text).correct())
        
        # Lowercase
        corrected_text = corrected_text.lower()

        # Remove accents
        corrected_text = unicodedata.normalize('NFKD', corrected_text)
        corrected_text = ''.join([c for c in corrected_text if not unicodedata.combining(c)])
        
        # Remove non-alphanumeric characters (except spaces)
        corrected_text = re.sub(r'[^a-z0-9\s]', '', corrected_text)
        
        # Remove extra whitespace
        corrected_text = re.sub(r'\s+', ' ', corrected_text).strip()

        return corrected_text

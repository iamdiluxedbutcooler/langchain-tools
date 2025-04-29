from langchain.tools import BaseTool
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

class InputCompressorTool(BaseTool):
    name = "input_compressor"
    description = "Compresses long text input to keep only essential information."

    def _run(self, text: str) -> str:
        return self.compress(text)

    def _arun(self, text: str) -> str:
        raise NotImplementedError("InputCompressorTool does not support async.")

    @staticmethod
    def compress(text: str) -> str:
        parser = PlaintextParser.from_string(text, Tokenizer("english"))
        summarizer = LsaSummarizer()
        summary = summarizer(parser.document, sentences_count=3)
        return ' '.join(str(s) for s in summary)

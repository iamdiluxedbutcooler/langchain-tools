# langchain-tools 🦜🔗
Just a bunch of small tools I made and used to improve how LangChain agents process and understand text. These are lightweight, fast, and easy to plug into your existing LangChain workflows.  All tools inherit from `BaseTool` and can be dropped into LangChain agents immediately.

---

## Installation

```
pip install langchain openai textblob langdetect rake-nltk
```
Also, don’t forget to:
```
python -m textblob.download_corpora
```
(for TextBlob to work properly)

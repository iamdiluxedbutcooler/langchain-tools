# langchain-tools 🦜🔗
Just a bunch of small tools I made and used to improve how LangChain agents process and understand text.

These are lightweight, fast, and easy to plug into your existing LangChain workflows. 

---

## What's inside?

| Tool Name                     | What it does                                                      |
|------------------------------|-------------------------------------------------------------------|
| `TextSmartenerTool`          | Fixes spelling, normalizes text, removes noise                    |
| `EmotionClassifierTool`      | Guesses if input sounds happy, sad, angry, or neutral             |
| `IntentRecognizerTool`       | Figures out if the user is asking, requesting, complaining, etc.  |
| `LanguageQualityScorerTool`  | Gives a rough "how clean is this English?" score (0–100)          |
| `InputCompressorTool`        | Extractively summarizes long inputs to stay under token limits     |
| `PromptSanitizerTool`        | Removes prompt injection / jailbreak patterns from text           |
| `QuestionTypeClassifierTool` | Identifies the kind of question (factual, causal, compare, etc.)  |
| `TimeReferenceClassifierTool`| Detects if input refers to past, present, future, or is timeless  |

All tools inherit from `BaseTool` and can be dropped into LangChain agents immediately.

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

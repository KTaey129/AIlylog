# Day 1: Kickoff

I started a project to work through on my journey to become an AI engineer: **workout-recommender**.

## Project setup

I used `uv` to organize and initiate the project.

```bash
mkdir workout-recommender && cd workout-recommender
git init
uv init   # or: python -m venv .venv && source .venv/bin/activate
echo ".env" >> .gitignore
echo "__pycache__/" >> .gitignore
echo ".venv/" >> .gitignore
touch README.md .env
```

## First API call

I made my first API call using Anthropic's SDK.

```python
import anthropic, os
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic()
msg = client.messages.create(
    model="claude-sonnet-5",
    max_tokens=100,
    messages=[{"role": "user", "content": "Say hello in one sentence."}]
)
print(msg.content[0].text)
```

Response:

> Hi there! How's it going? What can I help you with today?

## Wrap-up

Lastly, I committed what I'd done and created a repo on my GitHub: [workout-recommender](https://github.com/KTaey129/workout-recommender).

# Course Log: Prompt Engineering for Developers (cont.)

## Iterative Prompt Development

Prompt engineering is rarely right on the first try — treat it like any other iterative process:

1. **Try something** — write an initial prompt and see what comes back.
2. **Analyze** where the result falls short of what you want (too long, wrong focus, wrong format, etc.).
3. **Clarify instructions**, or give the model more room to think through the problem before answering.
4. **Refine** the prompt, then re-test it against a batch of examples — a fix that works on one input can still break on the next, so a single example is never enough to call a prompt "done."

## Summarizing

A plain "summarize" instruction tends to pull in whatever the source text talks about, even topics unrelated to what you actually care about. Asking the model to **extract** instead of summarize keeps the output scoped to the information you actually need.

```python
prod_review = """
Got this panda plush toy for my daughter's birthday, \
who loves it and takes it everywhere. It's soft and \
super cute, and its face has a friendly look. It's \
a bit small for what I paid though. I think there \
might be other options that are bigger for the \
same price. It arrived a day earlier than expected, \
so I got to play with it myself before I gave it \
to her.
"""

prompt = f"""
Your task is to extract relevant information from \
a product review from an ecommerce site to give \
feedback to the Shipping department.

From the review below, delimited by triple quotes \
extract the information relevant to shipping and \
delivery. Limit to 30 words.

Review: ```{prod_review}```
"""

response = get_completion(prompt)
print(response)
```

## Next up

Inferring (sentiment, topics) from text.

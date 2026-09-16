# Textbook Log: AI Engineering

## Core concepts

- **Language model**: encodes statistical information about one or more languages.
- **Token**: a tiny, meaningful unit used by the model to separate context. A token is typically shorter than 3/4 of a word.
- **Masked LM**: predicts a word using both its predecessor and descendant context.
- **Autoregressive LM**: most language models today; predicts the next word using only prior context.

## Language modeling in the ML landscape

Language modeling is just one branch of ML algorithms. Other examples of ML applications:

- Recommender systems
- Stock price forecasting
- Object detection

## Self-supervision — why language models are special

- **Supervision**: training ML algorithms with labeled data — expensive, time-consuming, and a bottleneck.
- **Self-supervision**: labels are inferred directly from the input data.
- Inferred labels are abundant in the world (Reddit, articles, etc.), which is what makes Large Language Models possible.

## On model size

More parameters generally means a larger model, but "large" isn't a fixed, scientific threshold — today's "large" models will look small in the future.

## Common AI engineering techniques

- RAG (Retrieval-Augmented Generation)
- Fine-tuning
- Prompt engineering

## Foundation models

Foundation models are the base models everything else is built on — think ChatGPT, Claude, Gemini.

**AI engineering** refers to building applications on top of foundation models.

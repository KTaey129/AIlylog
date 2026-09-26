# Textbook Log: AI Engineering (cont.)

## Pre-training vs. post-training

- **Pre-training** makes a model *capable* — it learns language, world knowledge, and reasoning patterns from raw text — but not necessarily *safe* or aligned with what users actually want.
- **Post-training** aligns the model with human preferences (helpfulness, harmlessness, instruction-following) on top of that raw capability.

## Data quality over data quantity

A smaller model trained on higher-quality data can beat a larger model trained on noisier data. "Quality" here means signal that's actually useful for the task, not just more tokens.

## Scaling, in three steps

1. Model performance depends on both model size and dataset size.
2. Bigger models and bigger datasets both require more compute to train.
3. Compute costs money — so scaling up is ultimately a cost decision, not just a capability one.

## Training workflow: pre-training → SFT → preference fine-tuning

1. **Self-supervised pre-training** — learn from raw, unlabeled text via next-token prediction.
2. **Supervised fine-tuning (SFT)** — fine-tune on curated instruction/response pairs (StackOverflow, Quora, human annotations, etc.) so the model learns to follow instructions.
3. **Preference fine-tuning** — further align outputs with human preferences, e.g. via RLHF.

## RLHF (Reinforcement Learning from Human Feedback)

1. Train a **reward model** that scores the foundation model's outputs (itself trained on human preference comparisons).
2. Optimize the foundation model with RL against that reward model, so it learns to generate responses that maximize the score.

## From logits to a response

Input → **logit vector** → probabilities → response.

- Each logit corresponds to exactly one token in the model's vocabulary.
- The logit vector is converted into a probability distribution over the vocabulary (softmax), and the next token is sampled from that distribution.

## Sampling

A language model's output is a sequence of tokens, and at every step the model computes a probability for each possible next token. How you sample from that distribution controls the coherence/creativity trade-off:

- **Temperature**: scales the logits before the softmax, applied at inference/sampling time (not during fine-tuning). Lower temperature sharpens the distribution toward the most likely tokens (more deterministic); higher temperature flattens it (more random, more "creative").
- **Top-k**: restrict sampling to the *k* most probable next tokens, then sample only among those.
- **Top-p (nucleus sampling)**: restrict sampling to the smallest set of tokens whose cumulative probability exceeds *p*, then sample among those — the candidate pool size adapts to how confident the model is at each step.
- **Stopping condition**: the rule that tells the model when to stop generating, e.g. reaching a max token count or producing an end-of-sequence/stop token.

## Structured outputs

Getting a model to output a fixed structure (JSON, a function-call schema, etc.) matters most in **agentic workflows**, where the model's output is often passed directly as input into tools the model calls — a malformed or unstructured output there breaks the tool call downstream.

# Textbook Log: AI Engineering (cont.)

## AI engineering vs. ML

AI engineering differs from traditional ML in that it's less about model
development and more about **adapting** foundation models to a task and
**evaluating** how well they perform.

## Prompt engineering vs. fine-tuning

- In many cases, prompt engineering can substitute for fine-tuning — it's
  cheaper and faster to iterate on, so it's usually worth trying first.
- Fine-tuning becomes necessary once prompting alone hits a ceiling (e.g.
  the task needs behavior or knowledge that can't be reliably coaxed out
  through instructions/examples alone).

## Open-ended vs. closed-ended tasks

- **Closed-ended**: output space is fixed/bounded (e.g. classification,
  multiple choice) — easier to evaluate automatically.
- **Open-ended**: output space is unbounded/generative (e.g. free-text
  answers, code generation) — harder to evaluate, often needs human or
  LLM-judge scoring.

## Prompt engineering is more than instructions

Prompt engineering isn't just telling the model what to do — it's also
giving the model:

- the necessary **context** to do the task
- the **tools** it needs to do the task

For complex tasks with long context, this can extend to giving the model
a **memory management system**, so it can keep track of its own history
across the interaction.

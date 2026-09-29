# Textbook Log: AI Engineering (cont.)

## Constrained sampling

Pipeline: Input → Model → logit vector → filter (apply constraints) → logits of valid tokens only → softmax → probabilities.

- **Softmax**: converts a vector of logits into a probability distribution — it exponentiates each logit and normalizes so the outputs sum to 1, so higher logits map to higher probabilities.
- Fine-tuning is generally more reliable than prompting for enforcing output constraints.
- As models improve, it should get easier to get models to output exactly what's needed with minimal prompting — these constraint techniques will likely matter less over time.

## The probabilistic nature of AI

Because models sample from a probability distribution rather than returning one fixed answer, this can cause **inconsistency** and **hallucination**:

- **Inconsistency**: the model gives a different output for the same prompt, or for a prompt with only a slight change.
- **Hallucination**: the model gives a response that isn't grounded in facts.

## Why hallucinations occur

1. **Self-delusion**: the model treats its own previously generated output as part of its input context. If it makes a wrong assumption early on, it keeps generating conditioned on that wrong assumption and justifying it — known as **snowballing hallucination**.
   - Can be mitigated with reinforcement learning or supervised fine-tuning.
2. **Knowledge difference between labelers and the model**: during fine-tuning, labelers may write responses based on knowledge the model itself doesn't have, teaching the model to answer confidently even when it lacks the underlying knowledge.

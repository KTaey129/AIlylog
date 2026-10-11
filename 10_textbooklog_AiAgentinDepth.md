# Textbook Log: AI Agent in Depth

## Practice comes first, name later

The author (a Pinecone engineering leader) argues that by the time a term is trending, leading companies have usually already worked through the problem it names. So how do you know what to do before the name arrives?

1. Have a real business that makes extreme demands on the agent's capability ceiling, and keep drawing genuine feedback from it.
2. Build an **evaluation mechanism**. Evaluation lets you tell whether a change is genuinely better or merely lucky, so the agent's direction of iteration no longer rests on gut feeling.

**Agent = LLM + Context + Tools** (all three are indispensable):
- **LLM**: the brain — decision making
- **Context**: the eyes (this is where RAG comes in) — what information the agent can see
- **Tools**: the hands & feet (MCP, async event architecture, tool security) — what the agent can actually do

AI agents are an intensely hands-on field — many design intuitions only take shape while debugging.

## Chapter 1. Getting started with AI agents

### What makes a system "agentic"

A typical agent system has:
- **Open-ended action space** — not picking from a fixed set of buttons, but generating arbitrary natural language and code
- **Internal reasoning** — planning before acting
- **Continuous interaction** — adjusting strategy based on environmental feedback

### Harness

The **harness** directs the model to work — it's not about limiting the model, but guiding it. It gets more important as models get more powerful.

- Does the harness get absorbed into the model itself as models improve? So far, no — the model can't internalize all the constraints and preferences of real businesses.

### The anatomy of an LLM call

Each LLM call has 5 components:
1. System prompt
2. Tool definitions — the agent's action capability
3. User messages
4. Assistant messages
5. Tool results — key to closed-loop control

Context determines what the agent can see, and the agent can only decide based on what it sees — but the components are not equivalent. "Produced an answer" is not "completed the task." When a context component is missing, the typical failure mode is not an error exit but an answer that looks flawless yet isn't.

### The ReAct loop

reason → act → observe → reason → act → observe

**Agent context = static prefix (system prompt + tool definitions) + trajectory**

The model may hallucinate (invent tools or parameters that don't exist), pick the wrong tool, or fail to recover from an error — this is why **harness engineering** exists: to fix these failure modes.

**Agent = Model + Harness**
**Harness = Context management + Tool interfaces + Constrain + Verify + Correct**
**Agent <> Environment**

The industry is shifting from *task completion* to *reliable* task completion, making harness engineering the core competitive advantage of agent systems.

### The five stages of AI application engineering

Prompt → Context → Harness → Loop → Graph

These are not replacements but **nested layers** — each layer widens the engineer's scope of concern and influence beyond the last.

### Core principles of building effective agents

1. **Keep it simple**: direct API calls, clear code, no extra layers of abstraction
2. **Keep it transparent**: expose the agent's planning steps, execution logs, and decision trajectory
3. **Design a well-structured tool interface**: design the interface from the agent's perspective

### How to choose a model

- **Closed-source** (OpenAI, Claude, etc.): don't trust the leaderboard — evaluate on your own tasks
- **Open-source**: lower cost, supports private deployment
- Beyond raw capability, consider the model's **policy boundaries** — for business-critical tasks, prepare a human handoff or a fallback compliant model
- Most agents need a model that supports reasoning
- Consider output speed and multimodal capabilities

A more complex harness isn't automatically a better one — the importance of the harness doesn't mean a *more complex* harness is better.

### Workflow pattern: deterministic orchestration

Orchestrates LLMs and tools through predefined code paths. Two core advantages:
- **Strict process control**: critical steps are never skipped
- **Security**: prompt injection or model error affects only the current node

Main limitation: lack of flexibility.

### Autonomous agent: runtime decision making

The execution path is determined at runtime by the agent, based on environmental feedback.

In practice, the two patterns aren't cleanly separated (e.g., n8n): critical processes run with strict workflow-style compliance, while dynamic, flexible decisions happen in autonomous mode.

### Guardrails and safety

How to constrain, verify, correct:
- **False refusal**: guardrail evaluation should test not only whether prohibited requests are blocked, but also whether clearly permitted requests can still be completed.

Guardrails can be set on three layers — **context, execution, data**:
- **Context layer**: relevance classifier, safety classifier, content moderation, rule-based protection (e.g., Anthropic's Constitutional Classifiers)

### Human intervention

**Human-in-the-loop** lets agents operate without degrading user experience. Two main situations that trigger human intervention:
- Exceeding failure thresholds — caps on agent retries and operations
- High-risk operations

## Chapter 2. Context Engineering

*(notes to come)*

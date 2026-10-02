# week1-structured-output

Week 1 build task: a script that takes messy free-text input and reliably returns
validated JSON, failing gracefully on malformed output.

Domain: parsing a free-text workout log entry ("did bench today, 3x8 @ 60kg") into a
structured `WorkoutEntry` (exercise, sets, reps, weight_kg).

## How it works

- `schema.py` — the `WorkoutEntry` Pydantic model, which doubles as the JSON schema
  handed to Claude and as the validator for whatever comes back.
- `extractor.py` — forces a tool call (`tool_choice`) against that schema instead of
  prompting for JSON and hoping. On a validation failure or a missing tool call, it
  retries with the error fed back into the next turn (`MAX_RETRIES = 2`). After
  retries are exhausted it returns `None` instead of raising.
- `main.py` — runs a handful of deliberately messy/invalid sample inputs through the
  extractor and prints the result (or the graceful failure).

## Run it

```bash
echo "ANTHROPIC_API_KEY=sk-ant-..." > .env
uv run main.py
```

## Test it

```bash
uv run pytest tests/ -v
```

Tests mock the Anthropic client, so they run free and deterministic — covering the
happy path, a retry-then-succeed path, exhausted retries, a model that never calls
the tool, and malformed tool input missing a required field.

**Done when:** fed genuinely messy input, it never raises an unhandled exception —
only valid `WorkoutEntry` JSON or a clean `None`.

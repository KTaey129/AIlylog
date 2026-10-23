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

## Results
input:  'did bench today, 3x8 @ 60kg, felt good'
output: {'exercise': 'bench press', 'sets': 3, 'reps': 8, 'weight_kg': 60.0}

input:  'squats 4 sets of 5 reps bodyweight only'
output: {'exercise': 'squats', 'sets': 4, 'reps': 5, 'weight_kg': None}

input:  'benchpress 5 sets 5 reps 100 kilos'
output: {'exercise': 'bench press', 'sets': 5, 'reps': 5, 'weight_kg': 100.0}

input:  'ran 5k in 25 minutes'
output: {'exercise': 'running', 'sets': 1, 'reps': 1, 'weight_kg': None}

input:  'did some deadlifts, lost count of sets, maybe heavy'
output: {'exercise': 'deadlift', 'sets': 1, 'reps': 1, 'weight_kg': None}

input:  'curls -3 sets of 10 reps at -5kg'
output: {'exercise': 'curls', 'sets': 3, 'reps': 10, 'weight_kg': 5.0}
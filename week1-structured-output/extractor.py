import logging

from anthropic import Anthropic
from pydantic import ValidationError

from schema import WorkoutEntry

logger = logging.getLogger(__name__)

MODEL = "claude-sonnet-5"
TOOL_NAME = "record_workout_entry"
MAX_RETRIES = 2

_TOOL_SCHEMA = {
    "name": TOOL_NAME,
    "description": "Record a single structured workout log entry.",
    "input_schema": WorkoutEntry.model_json_schema(),
}


def _call_claude(client: Anthropic, raw_input: str, error_context: str | None) -> dict | None:
    user_content = raw_input
    if error_context:
        user_content = f"{raw_input}\n\n(Your previous attempt failed: {error_context}. Fix it and try again.)"

    response = client.messages.create(
        model=MODEL,
        max_tokens=512,
        tools=[_TOOL_SCHEMA],
        tool_choice={"type": "tool", "name": TOOL_NAME},
        messages=[{"role": "user", "content": user_content}],
    )

    for block in response.content:
        if block.type == "tool_use" and block.name == TOOL_NAME:
            return block.input

    return None


def extract_workout_entry(
    client: Anthropic, raw_input: str, max_retries: int = MAX_RETRIES
) -> WorkoutEntry | None:
    """Parse messy free-text into a validated WorkoutEntry, or None on repeated failure."""
    error_context: str | None = None

    for attempt in range(max_retries + 1):
        tool_input = _call_claude(client, raw_input, error_context)

        if tool_input is None:
            error_context = "model did not call the required tool"
            logger.warning("attempt %d: %s", attempt, error_context)
            continue

        try:
            return WorkoutEntry.model_validate(tool_input)
        except ValidationError as exc:
            error_context = str(exc)
            logger.warning("attempt %d: validation failed: %s", attempt, error_context)

    logger.error("giving up on input after %d attempts: %r", max_retries + 1, raw_input)
    return None

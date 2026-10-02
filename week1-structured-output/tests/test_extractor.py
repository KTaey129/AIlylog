from types import SimpleNamespace
from unittest.mock import MagicMock

from extractor import extract_workout_entry
from schema import WorkoutEntry


def _tool_use_response(tool_input: dict) -> SimpleNamespace:
    block = SimpleNamespace(type="tool_use", name="record_workout_entry", input=tool_input)
    return SimpleNamespace(content=[block])


def _no_tool_call_response() -> SimpleNamespace:
    block = SimpleNamespace(type="text", name=None, input=None)
    return SimpleNamespace(content=[block])


def test_returns_validated_entry_on_first_valid_response():
    # Arrange
    client = MagicMock()
    client.messages.create.return_value = _tool_use_response(
        {"exercise": "bench press", "sets": 3, "reps": 8, "weight_kg": 60}
    )

    # Act
    result = extract_workout_entry(client, "did bench today, 3x8 @ 60kg")

    # Assert
    assert result == WorkoutEntry(exercise="bench press", sets=3, reps=8, weight_kg=60)
    assert client.messages.create.call_count == 1


def test_retries_after_validation_error_then_succeeds():
    # Arrange
    client = MagicMock()
    client.messages.create.side_effect = [
        _tool_use_response({"exercise": "curls", "sets": -3, "reps": 10, "weight_kg": -5}),  # invalid
        _tool_use_response({"exercise": "curls", "sets": 3, "reps": 10, "weight_kg": 5}),  # fixed
    ]

    # Act
    result = extract_workout_entry(client, "curls -3 sets of 10 reps at -5kg")

    # Assert
    assert result == WorkoutEntry(exercise="curls", sets=3, reps=10, weight_kg=5)
    assert client.messages.create.call_count == 2


def test_returns_none_when_validation_fails_every_retry():
    # Arrange
    client = MagicMock()
    client.messages.create.return_value = _tool_use_response(
        {"exercise": "curls", "sets": -3, "reps": 10, "weight_kg": -5}
    )

    # Act
    result = extract_workout_entry(client, "curls -3 sets of 10 reps at -5kg", max_retries=2)

    # Assert
    assert result is None
    assert client.messages.create.call_count == 3  # 1 initial + 2 retries


def test_returns_none_when_model_never_calls_the_tool():
    # Arrange
    client = MagicMock()
    client.messages.create.return_value = _no_tool_call_response()

    # Act
    result = extract_workout_entry(client, "unrelated chit-chat", max_retries=1)

    # Assert
    assert result is None
    assert client.messages.create.call_count == 2


def test_does_not_raise_on_malformed_tool_input_missing_required_field():
    # Arrange
    client = MagicMock()
    client.messages.create.return_value = _tool_use_response({"sets": 3, "reps": 8})  # missing "exercise"

    # Act
    result = extract_workout_entry(client, "3x8 of something, forgot what", max_retries=0)

    # Assert
    assert result is None

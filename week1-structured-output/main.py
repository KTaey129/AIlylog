import logging
import os

from anthropic import Anthropic
from dotenv import load_dotenv

from extractor import extract_workout_entry

SAMPLE_INPUTS = [
    "did bench today, 3x8 @ 60kg, felt good",
    "squats 4 sets of 5 reps bodyweight only",
    "benchpress 5 sets 5 reps 100 kilos",
    "ran 5k in 25 minutes",  # not a strength entry — should still produce *something* or fail cleanly
    "did some deadlifts, lost count of sets, maybe heavy",  # genuinely ambiguous / missing data
    "curls -3 sets of 10 reps at -5kg",  # invalid: negative sets/weight
]


def main() -> None:
    load_dotenv()
    logging.basicConfig(level=logging.WARNING)

    client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

    for raw_input in SAMPLE_INPUTS:
        entry = extract_workout_entry(client, raw_input)
        print(f"input:  {raw_input!r}")
        print(f"output: {entry.model_dump() if entry else 'FAILED (gracefully)'}")
        print()


if __name__ == "__main__":
    main()

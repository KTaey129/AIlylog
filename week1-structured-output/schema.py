from pydantic import BaseModel, Field


# Subclassing BaseModel is what gives WorkoutEntry its validation methods for free —
# model_json_schema() and model_validate() (used in extractor.py) aren't defined here;
# they're inherited from BaseModel and introspect whatever fields this class declares.
class WorkoutEntry(BaseModel):
    exercise: str = Field(description="Exercise name, normalized (e.g. 'bench press' not 'benchpress')")
    sets: int = Field(gt=0, description="Number of sets performed")
    reps: int = Field(gt=0, description="Number of reps per set")
    weight_kg: float | None = Field(default=None, ge=0, description="Weight used in kilograms, null if bodyweight")

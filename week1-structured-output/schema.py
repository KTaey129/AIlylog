from pydantic import BaseModel, Field


class WorkoutEntry(BaseModel):
    exercise: str = Field(description="Exercise name, normalized (e.g. 'bench press' not 'benchpress')")
    sets: int = Field(gt=0, description="Number of sets performed")
    reps: int = Field(gt=0, description="Number of reps per set")
    weight_kg: float | None = Field(default=None, ge=0, description="Weight used in kilograms, null if bodyweight")

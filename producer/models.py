from typing import Literal
from pydantic import BaseModel, Field

class Alert(BaseModel):
    border: Literal["egypt", "lebanon", "gaza", "syria", "jordan"]
    zone: str
    timestamp: str
    people_count: int
    weapons_count: int
    vehicle_type:  Literal["motorcycle", "jeep", "truck", "car", None]
    distance_from_fence_m: int
    visibility_quality: int | float = Field(gt=0, lt=100)

from pydantic import BaseModel
from typing import Optional
from ..models.diary import Emotion


class EmotionRetrieveRequestDto(BaseModel):
    day: Optional[int]


class EmotionRetrieveResponseDto(BaseModel):
    emotion: Emotion
    value: float
    date: str

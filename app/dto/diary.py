from typing import List, Optional
from pydantic import BaseModel
from ..models.diary import Emotion

# request
class DiaryCreateRequestDto(BaseModel):
    context: str
    emotion: Emotion
    value: float
    date: str


class DiaryListRequestDto(BaseModel):
    user_id: int
    year: Optional[int] = None
    month: Optional[int] = None


class DiaryRetrieveRequestDto(BaseModel):
    diary_id: int


class DiaryUpdateRequestDto(BaseModel):
    context: str
    emotion: Emotion
    value: float


# response
class DiaryCreateResponseDto(BaseModel):
    diary_id: int
    context: str
    emotion: Emotion
    value: float
    date: str
    created_at: str
    photos: list


class DiaryListResponseDto(BaseModel):
    diary_id: int
    date: str


class DiaryRetrieveResponseDto(BaseModel):
    diary_id: int
    context: str
    emotion: Emotion
    value: float
    date: str
    created_at: str
    photos: list


class DiaryCardListResponseDto(BaseModel):
    year: int
    month: int


class DiaryCountResponseDto(BaseModel):
    count: int


class DiaryUpdateResponseDto(BaseModel):
    diary_id: int
    context: str
    emotion: Emotion
    value: float
    date: str
    created_at: str
    photos: list


class DiaryDeleteResponseDto(BaseModel):
    message: str

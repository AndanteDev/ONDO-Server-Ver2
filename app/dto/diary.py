from app import create_app
from typing import List, Optional
from pydantic import BaseModel
from ..models.diary import Emotion
from fastapi import File, UploadFile

# request
class DiaryCreateRequestDto(BaseModel):
    context: str
    emotion: Emotion
    value: float
    date: str
    photos: Optional[List[UploadFile]] = []


class DiaryListRequestDto(BaseModel):
    year: Optional[int]
    month: Optional[int]


class DiaryRetrieveRequestDto(BaseModel):
    diary_id: int


class DiaryCardListRequesteDto(BaseModel):
    pass


class DiaryCountRequestDto(BaseModel):
    pass


class DiaryUpdateRequestDto(BaseModel):
    context: str
    emotion: Emotion
    value: float


class DiaryDeleteRequestDto(BaseModel):
    pass


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

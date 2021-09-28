from typing import List, Optional
from pydantic import BaseModel
from ..models.diary import Emotion
from fastapi import File, UploadFile

# request
class DiaryCreateRequestDto(BaseModel):
    context: str
    emotion: Emotion
    value: float
    photos: Optional[List[UploadFile]]


class DiaryListRequestDto(BaseModel):
    year: Optional[int]
    month: Optional[int]


class DiaryRetrieveRequestDto(BaseModel):
    pass


class DiaryCardListRequesteDto(BaseModel):
    pass


class DiaryCountRequestDto(BaseModel):
    pass


class DiaryUpdateRequestDto(BaseModel):
    pass


class DiaryDeleteRequestDto(BaseModel):
    pass


# response
class DiaryCreateResponseDto(BaseModel):
    pass


class DiaryListResponseDto(BaseModel):
    pass


class DiaryRetrieveResponseDto(BaseModel):
    pass


class DiaryCardListResponseDto(BaseModel):
    pass


class DiaryCountResponseDto(BaseModel):
    pass


class DiaryUpdateResponseDto(BaseModel):
    pass


class DiaryDeleteResponseDto(BaseModel):
    pass

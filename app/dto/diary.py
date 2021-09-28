from typing import Optional
from pydantic import BaseModel

# request
class DiaryCreateRequestDto(BaseModel):
    pass


class DiaryListRequestDto(BaseModel):
    pass


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

from typing import Optional, List
from starlette import status
from fastapi import APIRouter, Request, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from ..dto.diary import (
    DiaryCardListResponseDto,
    DiaryCountResponseDto,
    DiaryCreateResponseDto,
    DiaryCreateRequestDto,
    DiaryDeleteResponseDto,
    DiaryListRequestDto,
    DiaryListResponseDto,
    DiaryRetrieveRequestDto,
    DiaryRetrieveResponseDto,
    DiaryUpdateRequestDto,
    DiaryUpdateResponseDto,
)
from ..service.diary_service import get_all_diaries

router = APIRouter()
security = HTTPBearer()


@router.get(
    "/diary",
    response_model=List[DiaryListResponseDto],
    status_code=status.HTTP_200_OK,
)
def list_diary(
    request: Request, year: Optional[int] = None, month: Optional[int] = None
):
    input_dto = DiaryListRequestDto(user_id=1, year=year, month=month)
    return get_all_diaries(input_dto)

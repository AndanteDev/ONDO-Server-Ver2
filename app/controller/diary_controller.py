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
from ..service.diary_service import get_all_diaries, save_new_diary

router = APIRouter()
security = HTTPBearer()


@router.get(
    "/diary",
    response_model=List[DiaryListResponseDto],
    status_code=status.HTTP_200_OK,
    tags=["diary"],
)
def list_diary(
    request: Request, year: Optional[int] = None, month: Optional[int] = None
) -> List[DiaryListResponseDto]:
    input_dto = DiaryListRequestDto(user_id=1, year=year, month=month)
    return get_all_diaries(input_dto)


@router.post(
    "/diary",
    response_model=DiaryCreateResponseDto,
    status_code=status.HTTP_201_CREATED,
    tags=["diary"],
)
def create_new_diary(
    request: Request, input_dto: DiaryCreateRequestDto
) -> DiaryCreateResponseDto:

    user_id = 1

    return save_new_diary(user_id, input_dto)

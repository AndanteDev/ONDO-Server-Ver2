from typing import Optional, List
from sqlalchemy.sql.expression import delete
from starlette import status
from fastapi import APIRouter, Request, Security
from fastapi import File, UploadFile, Form
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
from ..service.diary_service import (
    get_all_diaries,
    save_new_diary,
    get_a_diary,
    delete_diary,
)
from ..models.diary import Emotion

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


@router.get(
    "/diary/{diary_id}",
    response_model=DiaryRetrieveResponseDto,
    status_code=status.HTTP_200_OK,
    tags=["diary"],
)
def retrieve_diary(
    diary_id: int,
) -> DiaryRetrieveResponseDto:
    return get_a_diary(diary_id)


@router.post(
    "/diary",
    response_model=DiaryCreateResponseDto,
    status_code=status.HTTP_201_CREATED,
    tags=["diary"],
)
def create_new_diary(
    request: Request,
    context: str = Form(...),
    emotion: Emotion = Form(...),
    value: float = Form(...),
    date: str = Form(...),
    photos: List[UploadFile] = File(...),
) -> DiaryCreateResponseDto:

    user_id = 1
    input_dto = DiaryCreateRequestDto(
        context=context, emotion=emotion, value=value, date=date
    )

    return save_new_diary(user_id, input_dto, photos)


@router.delete(
    "/diary/{diary_id}",
    response_model=DiaryDeleteResponseDto,
    status_code=status.HTTP_200_OK,
    tags=["diary"],
)
def delete_a_diary(
    diary_id: int,
) -> DiaryDeleteResponseDto:
    return delete_diary(diary_id)

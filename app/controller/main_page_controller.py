from typing import Optional, List
from sqlalchemy.sql.expression import delete
from starlette import status
from fastapi import APIRouter, Request, Security
from fastapi import File, UploadFile, Form
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.dto.photo import RandomPhotoRetrieveDto
from app.service.photo_service import get_random_photo
from ..dto.emotion import EmotionRetrieveRequestDto, EmotionRetrieveResponseDto
from ..dto.diary import DiaryCountResponseDto
from ..service.emotion_service import get_emotions
from ..service.diary_service import count_diary
from ..models.diary import Emotion

router = APIRouter()
security = HTTPBearer()


@router.get("/count", status_code=status.HTTP_200_OK, tags=["main_page"])
def count_my_diaries(request: Request) -> DiaryCountResponseDto:
    return count_diary(1)


@router.get(
    "/emotion", response_model=List[EmotionRetrieveResponseDto], tags=["main_page"]
)
def list_emotions(day: Optional[int] = None) -> List[EmotionRetrieveResponseDto]:

    input_dto = EmotionRetrieveRequestDto(day=day)
    user_id = 1

    return get_emotions(user_id, input_dto)


@router.get("/random-photo", response_model=RandomPhotoRetrieveDto, tags=["main_page"])
def get_a_random_photo(reqeust: Request):
    user_id = 1
    return get_random_photo(user_id)

from typing import Optional, List
from sqlalchemy.sql.expression import delete
from starlette import status
from fastapi import APIRouter, Request, Security
from fastapi import File, UploadFile, Form
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from ..dto.emotion import EmotionRetrieveRequestDto, EmotionRetrieveResponseDto
from ..service.emotion_service import get_emotions
from ..models.diary import Emotion

router = APIRouter()
security = HTTPBearer()


@router.get(
    "/emotion", response_model=List[EmotionRetrieveResponseDto], tags=["main_page"]
)
def list_emotions(day: Optional[int] = None) -> List[EmotionRetrieveResponseDto]:

    input_dto = EmotionRetrieveRequestDto(day=day)
    user_id = 1

    return get_emotions(user_id, input_dto)

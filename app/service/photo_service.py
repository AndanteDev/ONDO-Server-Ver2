from ..db.session import db_session
from ..models.diary import Diary
from ..models.photo import Photo
from ..dto.photo import RandomPhotoRetrieveDto
from fastapi import HTTPException
from starlette import responses, status
import random


def get_random_photo(user_id) -> RandomPhotoRetrieveDto:

    photos = (
        db_session.query(Photo.url)
        .outerjoin(Diary, Diary.diary_id == Photo.diary_id)
        .filter(Diary.user_id == user_id)
        .all()
    )

    idx = random.randrange(0, len(photos))

    response = {"url": photos[idx][0]}

    return response

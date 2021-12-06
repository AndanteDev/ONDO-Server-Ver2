from ..db.session import db_session
from ..models.diary import Diary, Emotion
from ..dto.emotion import EmotionRetrieveRequestDto, EmotionRetrieveResponseDto
from fastapi import HTTPException
from starlette import responses, status


def get_emotions(
    user_id: int, input_dto: EmotionRetrieveRequestDto
) -> EmotionRetrieveResponseDto:

    day = input_dto.day

    if day != None:

        emotions = (
            db_session.query(Diary.emotion, Diary.value, Diary.date)
            .filter(Diary.user_id == user_id)
            .order_by(Diary.date.desc())
            .limit(day)
            .all()
        )

    else:

        emotions = (
            db_session.query(Diary.emotion, Diary.value, Diary.date)
            .filter(Diary.user_id == user_id)
            .order_by(Diary.date)
            .all()
        )

    response = [
        {"emotion": emotion.emotion, "value": emotion.value, "date": str(emotion.date)}
        for emotion in emotions[::-1]
    ]

    return response

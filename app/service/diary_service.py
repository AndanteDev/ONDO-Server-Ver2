from ..db.session import db_session
from ..models.diary import Diary
from ..models.photo import Photo
from ..utils.util import Util
from ..utils.exceptions import (
    FailToSaveChangeException,
    TodayDiaryAlreadyExistsException,
    FailToUploadImageFileException,
)
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
from datetime import datetime
from typing import Optional, List
from fastapi import File, UploadFile, HTTPException
from werkzeug.utils import secure_filename
import random
import string
from starlette import responses, status


def save_changes(data):
    try:
        db_session.add(data)
        db_session.commit()
    except Exception as e:
        raise HTTPException(status_code=409, detail="Fail to save change. Try again")


def delete_data(data):
    try:
        db_session.delete(data)
        db_session.commit()
    except Exception as e:
        raise HTTPException(status_code=409, detail="Fail to save change. Try again")


def save_new_diary(
    user_id: int, input_dto: DiaryCreateRequestDto, photos: List[UploadFile] = File(...)
) -> DiaryCreateResponseDto:

    today_diary = (
        db_session.query(Diary)
        .filter(Diary.user_id == user_id)
        .filter(Diary.date == input_dto.date)
        .first()
    )

    if today_diary is None:

        new_diary = Diary(
            user_id,
            input_dto.context,
            input_dto.emotion,
            input_dto.value,
            input_dto.date,
        )

        save_changes(new_diary)

    else:
        raise HTTPException(
            status_code=409, detail="Today diary already exists. Try tomorrow"
        )

    created_photos = []

    string_pool = string.ascii_letters + string.digits

    if len(photos) > 3:
        photos = photos[:3]

    try:

        for photo in photos:
            extension = secure_filename(photo.filename).split(".")[-1]
            file = photo.file

            filename = (
                str(datetime.now()).replace(" ", "").replace(".", "")
                + "".join([random.choice(string_pool) for _ in range(10)])
                + "."
                + extension
            )

            url = Util.s3upload(file, filename)
            new_photo = Photo(diary_id=new_diary.diary_id, filename=filename, url=url)
            save_changes(new_photo)

            created_photos.append(url)
    except:
        delete_data(new_diary)
        raise HTTPException(status_code=500, detail="Fail to upload Image. Try again")

    new_diary.photos = created_photos
    response = new_diary.to_dict()

    return DiaryCreateResponseDto(**response)


def get_all_diaries(input_dto: DiaryListRequestDto) -> DiaryListResponseDto:

    year = input_dto.year
    month = input_dto.month

    diary = []

    if year != None and month != None:
        start = str(year) + "-" + str(month).zfill(2) + "-01"
        end = str(year) + "-" + str(int(month) + 1).zfill(2) + "-01"
        diaries = (
            db_session.query(Diary.diary_id, Diary.date)
            .filter(Diary.date.between(start, end))
            .order_by(Diary.date)
            .all()
        )
    elif year != None and month == None:
        start = str(year) + "-01-01"
        end = str(int(year) + 1) + "-01-01"
        diaries = (
            db_session.query(Diary.diary_id, Diary.date)
            .filter(Diary.date.between(start, end))
            .order_by(Diary.date)
            .all()
        )
    else:
        diaries = (
            db_session.query(Diary.diary_id, Diary.date).order_by(Diary.date).all()
        )

    diary = [{"diary_id": diary.diary_id, "date": str(diary.date)} for diary in diaries]

    return diary


def get_a_diary(diary_id: int) -> DiaryRetrieveResponseDto:

    diary = db_session.query(Diary).filter(Diary.diary_id == diary_id).first()

    if not diary:
        raise HTTPException(status_code=404, detail="Diary not found.")

    photos = [
        url[0]
        for url in db_session.query(Photo.url).filter(Photo.diary_id == diary_id).all()
    ]

    response = {
        "diary_id": diary.diary_id,
        "context": diary.context,
        "emotion": int(diary.emotion),
        "value": diary.value,
        "date": str(diary.date),
        "created_at": str(diary.created_at),
        "photos": photos,
    }

    return DiaryRetrieveResponseDto(**response)


def delete_diary(diary_id: int) -> DiaryDeleteResponseDto:

    diary = db_session.query(Diary).filter(Diary.diary_id == diary_id).first()

    if not diary:
        raise HTTPException(status_code=404, detail="Diary not found.")

    photos = db_session.query(Photo.filename).filter(Photo.diary_id == diary_id).all()

    for photo in photos:
        Util.s3delete(photo[0])

    delete_data(diary)

    response = {"message": "Successfully deleted"}

    return response


def update_diary(
    diary_id: int, input_dto: DiaryUpdateRequestDto
) -> DiaryUpdateResponseDto:
    pass


def count_diary(user_id: int) -> DiaryCountResponseDto:
    pass

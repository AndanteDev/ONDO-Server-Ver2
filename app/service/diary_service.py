from ..db.session import db_session
from ..models.diary import Diary
from ..models.photo import Photo
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


def save_new_diary(input_dto: DiaryCreateRequestDto) -> DiaryCreateResponseDto:
    pass


def get_all_diaries(input_dto: DiaryListRequestDto) -> DiaryListResponseDto:
    year = input_dto.year
    month = input_dto.month

    diary = None

    if year != None and month != None:
        start = str(year) + "-" + str(month).zfill(2) + "-01"
        end = str(year) + "-" + str(int(month) + 1).zfill(2) + "-01"
        diaries = (
            db_session.query(Diary.diary_id, Diary.date)
            .filter(Diary.date.between(start, end))
            .all()
        )
    elif year != None and month == None:
        start = str(year) + "-01-01"
        end = str(int(year) + 1) + "-01-01"
        diaries = (
            db_session.query(Diary.diary_id, Diary.date)
            .filter(Diary.date.between(start, end))
            .all()
        )
    else:
        diaries = db_session.query(Diary.diary_id, Diary.date).all()

    diary = [{"diary_id": diary.diary_id, "date": str(diary.date)} for diary in diaries]

    return diary


def get_a_diary(
    diary_id: int, input_dto: DiaryRetrieveRequestDto
) -> DiaryRetrieveResponseDto:
    pass


def delete_diary(diary_id: int) -> DiaryDeleteResponseDto:
    pass


def update_diary(
    diary_id: int, input_dto: DiaryUpdateRequestDto
) -> DiaryUpdateResponseDto:
    pass


def count_diary(user_id: int) -> DiaryCountResponseDto:
    pass


def diary_card_list(user_id: int) -> DiaryCardListResponseDto:
    pass


def save_changes(data):
    try:
        db_session.add(data)
        db_session.commit()
    except Exception as e:
        print(e)

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
    pass


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

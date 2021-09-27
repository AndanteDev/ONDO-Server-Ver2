from datetime import datetime
from sqlalchemy import Column, Integer, Float, TEXT, DateTime, Date, Enum
from ..db.session import Base
import enum


class Emotion(enum.IntEnum):
    happy = 1
    sad = 2
    angry = 3
    soso = 4
    tired = 5


class Diary(Base):
    __tablename__ = "diary"

    diary_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    context = Column(TEXT)
    emotion = Column(Enum(Emotion))
    value = Column(Float)
    date = Column(Date)
    created_at = Column(DateTime, nullable=False)

    def __init__(self, user_id, context, emotion, value, date):
        self.diary_id = None
        self.user_id = user_id
        self.context = context
        self.emotion = emotion
        self.value = value
        self.date = date
        self.created_at = datetime.now()

    def __repr__(self):
        return "<Diary '{},{}'>".format(self.user_id, self.date)

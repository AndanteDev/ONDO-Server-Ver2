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
    date = Column(Date, nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=str(datetime.now()))

    def __init__(self, user_id, context, emotion, value, date):
        self.diary_id = None
        self.user_id = user_id
        self.context = context
        self.emotion = emotion
        self.value = value
        self.date = date
        self.created_at = datetime.now()
        self.photos = []

    def to_dict(self):
        return {
            "diary_id": self.diary_id,
            "user_id": self.user_id,
            "context": self.context,
            "emotion": self.emotion,
            "value": self.value,
            "date": str(self.date),
            "created_at": str(self.created_at),
            "photos": self.photos,
        }

    def __repr__(self):
        return "<Diary '{},{}'>".format(self.user_id, self.date)

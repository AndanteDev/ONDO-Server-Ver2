from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.schema import ForeignKey
from ..db.session import Base
from .diary import Diary


class Photo(Base):

    __tablename__ = "photo"

    photo_id = Column(Integer, primary_key=True, autoincrement=True)
    diary_id = Column(ForeignKey(Diary.diary_id, ondelete="CASCADE"), nullable=False)
    filename = Column(String(256), nullable=False)
    url = Column(String(256), nullable=False)

    def __init__(self, diary_id, url):
        self.photo_id = None
        self.diary_id = diary_id
        self.url = url

    def __repr__(self):
        return "<Photo '{}'>".format(self.url)

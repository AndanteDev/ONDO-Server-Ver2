from app import create_app
from typing import List, Optional
from pydantic import BaseModel


class RandomPhotoRetrieveDto(BaseModel):
    url: str

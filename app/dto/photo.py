from pydantic import BaseModel


class RandomPhotoRetrieveDto(BaseModel):
    url: str

from datetime import datetime

from pydantic import BaseModel


class PostBase(BaseModel):
    title: str
    text: str
    date: datetime

    class ConfigDict:
        from_attributes = True


class PostList(PostBase):
    id: int


class PostCreate(PostBase):
    pass

from typing import List

from pydantic import BaseModel, HttpUrl


class Short(BaseModel):
    id: int
    videoUrl: HttpUrl
    title: str
    tags: List[str]


class ShortCreate(BaseModel):
    videoUrl: HttpUrl
    title: str
    tags: List[str]

from typing import List

from pydantic import BaseModel, field_validator


class Short(BaseModel):
    id: int
    videoUrl: str
    title: str
    tags: List[str]


class ShortCreate(BaseModel):
    videoUrl: str
    title: str
    tags: List[str]

    @field_validator("videoUrl")
    @classmethod
    def validate_url(cls, v: str) -> str:
        v = v.strip()
        if not v.startswith(("http://", "https://")):
            raise ValueError("URL must start with http:// or https://")
        return v

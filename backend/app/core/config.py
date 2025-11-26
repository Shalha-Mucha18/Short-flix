from functools import lru_cache
from typing import List

from pydantic import AnyHttpUrl
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Short-flix API"
    api_v1_prefix: str = "/api"
    allowed_hosts: List[AnyHttpUrl] = []


@lru_cache
def get_settings() -> Settings:
    return Settings()

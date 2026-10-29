import os
from typing import Literal

from pydantic import PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings, read only from CROSSPART_* environment variables."""

    model_config = SettingsConfigDict(env_prefix="CROSSPART_", extra="ignore")

    environment: Literal["local", "ci", "production"] = "local"
    database_url: PostgresDsn


def get_settings() -> Settings:
    return Settings()

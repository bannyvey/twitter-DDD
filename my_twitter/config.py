import os
from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

STATIC = "/app/static"
PATH_MEDIA = os.path.join(STATIC, "images")
BASE_DIR = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    db_user: str = Field(validation_alias="DB_USER")
    db_password: str = Field(validation_alias="DB_PASSWORD")
    db_name: str = Field(validation_alias="DB_NAME")
    db_host: str = Field(validation_alias="DB_HOST")
    db_port: int = Field(validation_alias="DB_PORT")
    
    # JWT settings
    jwt_secret_key: str = "your-secret-key-change-in-production"
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    refresh_token_expire_days: int = 7

    model_config = SettingsConfigDict(

        env_file=BASE_DIR / ".env",
        extra="ignore",
        env_file_encoding="utf-8",
    )


settings = Settings()

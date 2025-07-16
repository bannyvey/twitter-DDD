import os

from pydantic_settings import BaseSettings, SettingsConfigDict

STATIC = "/app/static"
PATH_MEDIA = os.path.join(STATIC, "images")


class Settings(BaseSettings):
    db_user: str
    db_password: str
    db_name: str
    db_host: str
    db_port: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()

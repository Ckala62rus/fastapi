from pydantic_settings import BaseSettings, SettingsConfigDict

from core.utils import BASE_DIR


class Settings(BaseSettings):
    SECRET: str
    ALGORITHM: str
    SQLALCHEMY_DATABASE_URL: str
    SQLALCHEMY_DATABASE_URL_FOR_ALEMBIC: str

    model_config = SettingsConfigDict(env_file=BASE_DIR / ".env", extra="ignore")


settings = Settings()

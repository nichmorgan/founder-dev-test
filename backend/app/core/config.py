from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import MongoDsn


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", frozen=True)

    PROJECT_NAME: str = "backend"
    API_STR: str = "/api"
    MONGO_DATABASE_DSN: MongoDsn
    MONGO_DATABASE_NAME: str


settings = Settings()  # type: ignore

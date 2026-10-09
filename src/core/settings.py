from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import URL


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )

    log_level: str = "info"

    postgres_host: str
    postgres_db: str
    postgres_user: str
    postgres_password: SecretStr

    @property
    def postgres_url(self) -> str:
        return URL.create(
            "postgresql+asyncpg",
            username=self.postgres_user,
            password=self.postgres_password.get_secret_value(),
            host=self.postgres_host,
            port=5432,
            database=self.postgres_db,
        ).render_as_string(hide_password=False)


settings = Settings()

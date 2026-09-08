import os
from pathlib import Path

from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

PROJECT_ROOT = Path(__file__).resolve().parents[2]


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(PROJECT_ROOT / ".env", PROJECT_ROOT / "backend" / ".env"),
        extra="ignore",
    )

    gemini_api_key: str = ""
    gemini_base_url: str = ""
    gemini_model: str = "gemini-3.8-flash"
    embedding_model: str = "gemini-embedding-2"
    embedding_dim: int = 3072

    clickhouse_host: str = "localhost"
    clickhouse_port: int = 8123
    clickhouse_user: str = "shotmem"
    clickhouse_password: str = "shotmem"
    clickhouse_database: str = "shot_memory"
    clickhouse_secure: bool = False
    mcp_clickhouse_command: str = "mcp-clickhouse"

    data_dir: Path = PROJECT_ROOT / "data"
    ingest_concurrency: int = 8

    @field_validator("data_dir", mode="before")
    @classmethod
    def resolve_data_dir(cls, v: str | Path) -> Path:
        p = Path(v)
        return p if p.is_absolute() else (PROJECT_ROOT / p).resolve()

    def export_google_env(self) -> None:
        if self.gemini_api_key:
            os.environ.setdefault("GOOGLE_API_KEY", self.gemini_api_key)
        if self.gemini_base_url:
            os.environ.setdefault("GOOGLE_GEMINI_BASE_URL", self.gemini_base_url)
        os.environ.setdefault("GOOGLE_GENAI_USE_VERTEXAI", "FALSE")


settings = Settings()
settings.export_google_env()

"""Config."""
from typing import Any

from pydantic import BaseSettings, validator


class Settings(BaseSettings):

    VAPID_PUBLIC_KEY: str
    VAPID_PRIVATE_KEY: str
    VAPID_CLAIMS_SUB: str
    VAPID_CLAIMS: dict[str, Any] = None

    @validator("VAPID_CLAIMS", pre=True)
    def generate_first_superuser_data(
        cls, v: str | None, values: dict[str, Any]
    ) -> dict[str, Any]:
        if isinstance(v, dict):
            return v
        return {
            "sub": values["VAPID_CLAIMS_SUB"],
        }

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()

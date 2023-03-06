"""Config."""
from typing import Any

from pydantic import BaseSettings, root_validator, validator

from .utils import generate_vapid_keypair


class Settings(BaseSettings):

    API_PREFIX: str = "/api"
    VAPID_PUBLIC_KEY: str = None
    VAPID_PRIVATE_KEY: str = None
    VAPID_CLAIMS_SUB: str = "mailto:example@example.com"
    VAPID_CLAIMS: dict[str, Any] = None

    @root_validator
    def check_vapid_key(cls, values: dict[str, Any]):
        if not values.get("VAPID_PUBLIC_KEY") or not values.get("VAPID_PRIVATE_KEY"):
            key = generate_vapid_keypair()
            values["VAPID_PUBLIC_KEY"] = key["public_key"]
            values["VAPID_PRIVATE_KEY"] = key["private_key"]
        return values

    @validator("VAPID_CLAIMS", pre=True)
    def check_vapid_claims(
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

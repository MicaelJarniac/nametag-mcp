"""Settings for the Nametag MCP."""

from __future__ import annotations

__all__: tuple[str, ...] = ("settings",)

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Settings for the Nametag MCP."""

    api_url: str = "http://localhost:3000"
    openapi_url: str = "http://localhost:3000/api/openapi.json"


settings = Settings()

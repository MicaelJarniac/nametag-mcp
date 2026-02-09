"""Nametag MCP Server."""

from __future__ import annotations

__all__: tuple[str, ...] = ()

import httpx
from fastmcp import FastMCP

from nametag_mcp.settings import settings

client = httpx.AsyncClient(
    base_url=settings.api_url,
)

openapi_spec = httpx.get(settings.openapi_url).json()

mcp = FastMCP.from_openapi(
    openapi_spec=openapi_spec,
    client=client,
    name="Nametag",
)

if __name__ == "__main__":
    mcp.run(transport="http")

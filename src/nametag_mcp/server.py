"""Nametag MCP Server."""

from __future__ import annotations

__all__: tuple[str, ...] = ()

import httpx
from fastmcp import FastMCP

API_URL = "http://localhost:3000"

client = httpx.AsyncClient(
    base_url=API_URL,
    cookies={
        "authjs.session-token": "",
    },
)

openapi_spec = httpx.get(f"{API_URL}/api/openapi.json").json()

mcp = FastMCP.from_openapi(
    openapi_spec=openapi_spec,
    client=client,
    name="Nametag",
)

if __name__ == "__main__":
    mcp.run()

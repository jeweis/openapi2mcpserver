# server.py
"""
MCP服务器主模块，提供DEMO功能
"""

from typing import Dict, Any
from fastmcp import FastMCP

from typing import Dict, Any
from fastmcp import FastMCP

from .app_config import config
from .core import helloworld
import httpx

# 创建MCP服务器实例
# mcp = FastMCP(name=config.SERVER_NAME)


client = httpx.AsyncClient(base_url="https://api.jeweis.com")

openapi_spec = httpx.get("https://api.jeweis.com/api/v3/api-docs/default").json()

mcp = FastMCP.from_openapi(
    openapi_spec=openapi_spec,
    client=client,
    name="My API Server"
)


def main():
    """主函数，用于启动MCP服务器"""
    print("启动 MySQL MCP 服务器...")
    mcp.run()
    # To use a different transport, e.g., HTTP:
    # mcp.run(transport="streamable-http", host="127.0.0.1", port=9000)

if __name__ == "__main__":
    main()
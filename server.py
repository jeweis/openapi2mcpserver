# server.py
"""
MCP服务器主模块，提供openapi2mcp功能
"""

from fastmcp import FastMCP

from openapi2mcpserver.app_config import config
from openapi2mcpserver.core import helloworld
from fastmcp.server.openapi import RouteMap, MCPType
import httpx

# 创建MCP服务器实例
# mcp = FastMCP(name=config.SERVER_NAME)


client = httpx.AsyncClient(base_url=config.BASE_URL)

openapi_spec = httpx.get(config.OPEN_API_DOC_JSON_URL).json()

mcp = FastMCP.from_openapi(
    openapi_spec=openapi_spec,
    client=client,
    name="openapi2mcpserver server",
    route_maps=[
        RouteMap(
            methods=["GET"], 
            pattern=r"^/user/userManage/.*", 
            mcp_type=MCPType.TOOL,
        ),
        RouteMap(mcp_type=MCPType.EXCLUDE),
         ]
)


def main():
    """主函数，用于启动openapi2mcp服务器"""
    print("启动 openapi2mcpserver MCP 服务器...")
    # mcp.run()
    # To use a different transport, e.g., HTTP:
    mcp.run(transport="streamable-http", host="127.0.0.1", port=9087)

if __name__ == "__main__":
    main()
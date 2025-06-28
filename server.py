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

route_map_list=[]

# 从环境变量中读取路由配置
route_configs = config.get_route_maps()
for route_config in route_configs:
    route_map_list.append(RouteMap(
        methods=route_config['methods'],
        pattern=route_config['pattern'],
        mcp_type=MCPType.TOOL,
    ))

# 添加默认的排除规则
route_map_list.append(RouteMap(mcp_type=MCPType.EXCLUDE))

mcp = FastMCP.from_openapi(
    openapi_spec=openapi_spec,
    client=client,
    name="openapi2mcpserver server",
    route_maps=route_map_list
)


def main():
    """主函数，用于启动openapi2mcp服务器"""
    print("启动 openapi2mcpserver MCP 服务器...")
    # mcp.run()
    # To use a different transport, e.g., HTTP:
    mcp.run(transport="streamable-http", host="127.0.0.1", port=9087)

if __name__ == "__main__":
    main()
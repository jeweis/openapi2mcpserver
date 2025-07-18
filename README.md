# OpenAPI to MCP Server

这是一个OpenAPI转换服务器，提供了以下功能：

- 将OpenAPI规范转换为MCP服务
- 支持http header透传
- 支持本地mcp 通用stdio使用方式、也支持docker部署为mcp server后通过streamable http方式使用


## MCP 使用配置

本项目支持通过多种客户端配置 MCP 服务器，以便与各种 IDE 或工具集成。以下是一些常见客户端的配置示例：

### Windsurf / Cursor / Claude

对于基于 Windsurf 框架的客户端（如 Cursor 和 Claude），您可以在 `~/.codeium/windsurf/mcp_config.json` 文件中配置 MCP 服务器。以下是一个示例配置：

```json
{
  "mcpServers": {
    "openapi2mcpserver": {
      "disabled": false,
      "command": "uvx",
      "args": [
        "openapi2mcpserver"
      ],
      "env": {
        "BASE_URL": "your_openapi3.0_host",
        "OPEN_API_DOC_JSON_URL": "your_openapi3.0_host doc  json url"
      }
    }
  }
}
```

请将 `BASE_URL`, `OPEN_API_DOC_JSON_URL` 替换为您的实际 OpenAPI 服务器地址和文档 JSON URL。

### Cline

对于 Cline 客户端，您可以在其配置文件中添加类似的 MCP 服务器配置。具体的配置方式请参考 Cline 的官方文档。通常，您需要指定服务器的名称、命令、参数和环境变量。

```json
// Cline 配置文件示例 (具体格式请参考 Cline 文档)
{
  "mcpServers": {
    "openapi2mcpserver": {
      "command": "uvx",
      "args": [
        "openapi2mcpserver"
      ],
      "env": {
        "BASE_URL": "your_openapi3.0_host",
        "OPEN_API_DOC_JSON_URL": "your_openapi3.0_host doc  json url"
      }
    }
  }
}
```

请将示例中的占位符替换为您的实际 OpenAPI 服务器地址和文档 JSON URL，并根据 Cline 的具体配置格式进行调整。

## 安装

1. 克隆仓库
2. 安装依赖：`pip install -r requirements.txt`
3. 配置环境变量（参见下文）

## 配置

在项目根目录创建`.env`文件，包含以下环境变量：

```
BASE_URL=https://api.xxx.com
OPEN_API_DOC_JSON_URL=https://api.xxx.com/api/v3/api-docs/default
```

## 运行

### 使用uvx安装并运行（推荐）

```bash
uvx --from openapi2mcpserver
```

## docker部署方式

``` docker
docker run -d -p 9087:9087 -e BASE_URL=http://xxx.xx.xx.xxx:8044/xiaogj-ai-api -e OPEN_API_DOC_JSON_URL=http://xxx.xx.xx.xxx:8044/xiaogj-ai-api/v3/api-docs -e SERVER_NAME=OpenAPI2MCP-Docker-Server -e "ROUTE_MAPS=[{\"methods\":[\"GET\",\"POST\"],\"pattern\":\"^/tool/.*\"}]" jeweis/openapi2mcp:latest
```


### 说明
1. “xxx.xx.xx.xxx”需要换成本机ip
2. 环境变量按实际需求配置


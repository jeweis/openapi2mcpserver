# OpenAPI to MCP Server - Docker 部署指南

## 快速开始

1. **配置环境变量**
   ```bash
   cp .env.example .env
   # 编辑 .env 文件，填入您的 API 配置
   ```

2. **启动服务**
   ```bash
   docker-compose up -d
   ```

3. **查看日志**
   ```bash
   docker-compose logs -f
   ```

## 环境变量说明

- `BASE_URL`: OpenAPI 服务器基础 URL (必需)
- `OPEN_API_DOC_JSON_URL`: OpenAPI 文档 JSON URL (必需)
- `SERVER_NAME`: MCP 服务器名称 (可选)
- `ROUTE_MAPS`: 路由映射配置 JSON (可选)

## 访问服务

服务启动后可通过以下方式访问:
- HTTP: http://localhost:9087
- MCP 客户端连接: http://localhost:9087/mcp

## 常用命令

```bash
# 查看容器状态
docker-compose ps

# 重启服务
docker-compose restart

# 停止服务
docker-compose down

# 查看实时日志
docker-compose logs -f openapi2mcp

# 重新构建并启动
docker-compose up --build -d
```

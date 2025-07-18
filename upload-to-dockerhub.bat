@echo off
echo ================================
echo OpenAPI2MCP Docker镜像上传脚本
echo ================================

set /p DOCKER_USERNAME="请输入您的DockerHub用户名: "
set /p VERSION="请输入版本号 (默认为v1.0.0): "

if "%VERSION%"=="" set VERSION=v1.0.0

echo.
echo 正在为镜像添加标签...
docker tag openapi2mcp:latest %DOCKER_USERNAME%/openapi2mcp:latest
docker tag openapi2mcp:latest %DOCKER_USERNAME%/openapi2mcp:%VERSION%

echo.
echo 请先登录DockerHub...
docker login

echo.
echo 正在推送镜像到DockerHub...
docker push %DOCKER_USERNAME%/openapi2mcp:latest
docker push %DOCKER_USERNAME%/openapi2mcp:%VERSION%

echo.
echo 上传完成！
echo 您的镜像现在可以通过以下命令拉取：
echo docker pull %DOCKER_USERNAME%/openapi2mcp:latest
echo docker pull %DOCKER_USERNAME%/openapi2mcp:%VERSION%

pause 
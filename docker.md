# Docker 使用指南

> Docker 容器化平台的基本命令和操作指南

## 目录
- [安装与配置](#安装与配置)
- [镜像管理](#镜像管理)
- [容器管理](#容器管理)
- [网络管理](#网络管理)
- [数据卷管理](#数据卷管理)
- [Docker Compose](#docker-compose)
- [常用场景](#常用场景)
- [故障排查](#故障排查)
- [常用命令速查](#常用命令速查)

---

## 安装与配置

### Ubuntu/WSL 安装 Docker

```bash
# 更新软件包列表
sudo apt update

# 安装必要的依赖
sudo apt install -y ca-certificates curl gnupg lsb-release

# 添加 Docker 官方 GPG 密钥
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

# 添加 Docker 仓库
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# 安装 Docker Engine
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# 启动 Docker 服务
sudo systemctl start docker
sudo systemctl enable docker

# 验证安装
sudo docker --version
sudo docker run hello-world
```

### 配置用户权限（可选）

```bash
# 将当前用户添加到 docker 组（避免每次使用 sudo）
sudo usermod -aG docker $USER

# 重新登录或执行以下命令使权限生效
newgrp docker

# 验证（不需要 sudo）
docker ps
```

### 配置镜像加速（国内用户）

创建或编辑 `/etc/docker/daemon.json`：

```bash
sudo mkdir -p /etc/docker
sudo tee /etc/docker/daemon.json <<-'EOF'
{
  "registry-mirrors": [
    "https://docker.mirrors.ustc.edu.cn",
    "https://hub-mirror.c.163.com",
    "https://mirror.baidubce.com"
  ]
}
EOF

# 重启 Docker 服务
sudo systemctl daemon-reload
sudo systemctl restart docker
```

---

## 镜像管理

### 搜索镜像

```bash
# 搜索 Docker Hub 上的镜像
docker search nginx
docker search python

# 搜索指定数量的结果
docker search --limit 5 nginx
```

### 拉取镜像

```bash
# 拉取最新版本
docker pull nginx
docker pull python:3.11

# 拉取指定版本
docker pull nginx:1.25
docker pull python:3.11-slim

# 拉取指定平台的镜像
docker pull --platform linux/amd64 nginx
```

### 查看镜像

```bash
# 查看所有本地镜像
docker images
docker image ls

# 查看镜像详细信息
docker images --format "table {{.Repository}}\t{{.Tag}}\t{{.Size}}"

# 查看镜像历史
docker history nginx

# 查看镜像详细信息
docker inspect nginx
```

### 删除镜像

```bash
# 删除指定镜像
docker rmi nginx
docker image rm nginx

# 删除指定标签的镜像
docker rmi nginx:1.25

# 删除所有未使用的镜像
docker image prune

# 删除所有镜像（谨慎使用）
docker rmi $(docker images -q)

# 强制删除（即使有容器在使用）
docker rmi -f nginx
```

### 构建镜像

```bash
# 从 Dockerfile 构建镜像
docker build -t myapp:latest .

# 指定 Dockerfile 路径
docker build -f /path/to/Dockerfile -t myapp:latest .

# 构建时传递参数
docker build --build-arg VERSION=1.0 -t myapp:1.0 .

# 不使用缓存构建
docker build --no-cache -t myapp:latest .
```

### 导出和导入镜像

```bash
# 导出镜像为 tar 文件
docker save -o nginx.tar nginx:latest
docker save nginx:latest > nginx.tar

# 导入镜像
docker load -i nginx.tar
docker load < nginx.tar

# 导出多个镜像
docker save -o images.tar nginx:latest python:3.11
```

### 标记镜像

```bash
# 为镜像打标签
docker tag nginx:latest myregistry.com/nginx:v1.0

# 查看镜像标签
docker images nginx
```

---

## 容器管理

### 运行容器

```bash
# 运行容器（前台运行）
docker run nginx

# 运行容器（后台运行）
docker run -d nginx
docker run --detach nginx

# 运行容器并指定名称
docker run -d --name my-nginx nginx

# 运行容器并映射端口
docker run -d -p 8080:80 nginx
docker run -d -p 127.0.0.1:8080:80 nginx

# 运行容器并挂载数据卷
docker run -d -v /host/path:/container/path nginx
docker run -d -v myvolume:/container/path nginx

# 运行容器并设置环境变量
docker run -d -e MYSQL_ROOT_PASSWORD=123456 mysql

# 运行容器并进入交互模式
docker run -it python:3.11 bash
docker run -it --rm python:3.11 python

# 运行容器并指定工作目录
docker run -d -w /app nginx

# 运行容器并指定用户
docker run -d -u 1000:1000 nginx

# 运行容器并设置资源限制
docker run -d --memory="512m" --cpus="1.0" nginx
```

### 查看容器

```bash
# 查看运行中的容器
docker ps

# 查看所有容器（包括已停止）
docker ps -a

# 查看容器详细信息
docker inspect my-nginx

# 查看容器日志
docker logs my-nginx

# 实时查看容器日志
docker logs -f my-nginx

# 查看最近 100 行日志
docker logs --tail 100 my-nginx

# 查看容器资源使用情况
docker stats

# 查看指定容器的资源使用
docker stats my-nginx

# 查看容器进程
docker top my-nginx
```

### 容器操作

```bash
# 启动已停止的容器
docker start my-nginx

# 停止运行中的容器
docker stop my-nginx

# 重启容器
docker restart my-nginx

# 暂停容器
docker pause my-nginx

# 恢复暂停的容器
docker unpause my-nginx

# 进入运行中的容器
docker exec -it my-nginx bash
docker exec -it my-nginx sh

# 在容器中执行命令
docker exec my-nginx ls -la
docker exec my-nginx python --version

# 删除容器
docker rm my-nginx

# 强制删除运行中的容器
docker rm -f my-nginx

# 删除所有已停止的容器
docker container prune

# 删除所有容器（谨慎使用）
docker rm $(docker ps -aq)
```

### 容器与主机文件互传

```bash
# 从容器复制文件到主机
docker cp my-nginx:/etc/nginx/nginx.conf ./nginx.conf

# 从主机复制文件到容器
docker cp ./file.txt my-nginx:/app/file.txt

# 复制目录
docker cp my-nginx:/app/logs ./logs
```

### 导出和导入容器

```bash
# 导出容器为 tar 文件
docker export my-nginx > nginx-container.tar

# 导入容器（会创建镜像）
docker import nginx-container.tar my-nginx:imported

# 从容器创建新镜像
docker commit my-nginx my-nginx:v1.0
docker commit -m "Added custom config" my-nginx my-nginx:v1.0
```

---

## 网络管理

### 查看网络

```bash
# 查看所有网络
docker network ls

# 查看网络详细信息
docker network inspect bridge

# 查看容器网络信息
docker inspect my-nginx | grep -A 20 "Networks"
```

### 创建网络

```bash
# 创建桥接网络
docker network create mynetwork

# 创建自定义网络（指定子网）
docker network create --subnet=172.20.0.0/16 mynetwork

# 创建网络并指定驱动
docker network create --driver bridge mynetwork
```

### 连接容器到网络

```bash
# 运行容器时连接到网络
docker run -d --network mynetwork --name app1 nginx

# 将运行中的容器连接到网络
docker network connect mynetwork my-nginx

# 断开容器与网络的连接
docker network disconnect mynetwork my-nginx
```

### 删除网络

```bash
# 删除网络
docker network rm mynetwork

# 删除所有未使用的网络
docker network prune
```

### 常用网络类型

```bash
# bridge - 默认网络（容器间可通信）
docker network create --driver bridge mybridge

# host - 使用主机网络（性能最好，但隔离性差）
docker run -d --network host nginx

# none - 无网络
docker run -d --network none nginx

# overlay - 用于 Swarm 集群
docker network create --driver overlay myoverlay
```

---

## 数据卷管理

### 创建数据卷

```bash
# 创建数据卷
docker volume create myvolume

# 创建数据卷并指定驱动
docker volume create --driver local myvolume
```

### 查看数据卷

```bash
# 查看所有数据卷
docker volume ls

# 查看数据卷详细信息
docker volume inspect myvolume
```

### 使用数据卷

```bash
# 运行容器时挂载数据卷
docker run -d -v myvolume:/data nginx

# 挂载主机目录到容器
docker run -d -v /host/path:/container/path nginx

# 挂载为只读
docker run -d -v myvolume:/data:ro nginx

# 使用命名卷（推荐）
docker run -d --mount source=myvolume,target=/data nginx
```

### 删除数据卷

```bash
# 删除数据卷
docker volume rm myvolume

# 删除所有未使用的数据卷
docker volume prune

# 删除容器时同时删除关联的数据卷
docker rm -v my-nginx
```

### 备份和恢复数据卷

```bash
# 备份数据卷
docker run --rm -v myvolume:/data -v $(pwd):/backup ubuntu tar czf /backup/backup.tar.gz /data

# 恢复数据卷
docker run --rm -v myvolume:/data -v $(pwd):/backup ubuntu tar xzf /backup/backup.tar.gz -C /
```

---

## Docker Compose

### 基本使用

```bash
# 启动服务（后台运行）
docker compose up -d

# 启动服务（前台运行，查看日志）
docker compose up

# 停止服务
docker compose down

# 停止服务并删除数据卷
docker compose down -v

# 查看服务状态
docker compose ps

# 查看服务日志
docker compose logs

# 查看指定服务的日志
docker compose logs nginx

# 实时查看日志
docker compose logs -f

# 重启服务
docker compose restart

# 重启指定服务
docker compose restart nginx

# 构建镜像
docker compose build

# 强制重新构建
docker compose build --no-cache

# 执行命令
docker compose exec nginx bash

# 扩展服务实例
docker compose up -d --scale nginx=3
```

### docker-compose.yml 示例

```yaml
version: '3.8'

services:
  web:
    image: nginx:latest
    ports:
      - "8080:80"
    volumes:
      - ./html:/usr/share/nginx/html
    networks:
      - mynetwork
    environment:
      - NGINX_HOST=localhost
    depends_on:
      - db

  db:
    image: mysql:8.0
    environment:
      - MYSQL_ROOT_PASSWORD=123456
      - MYSQL_DATABASE=myapp
    volumes:
      - db_data:/var/lib/mysql
    networks:
      - mynetwork

volumes:
  db_data:

networks:
  mynetwork:
    driver: bridge
```

---

## 常用场景

### 运行 Web 服务器

```bash
# Nginx
docker run -d -p 8080:80 --name nginx nginx

# Apache
docker run -d -p 8080:80 --name apache httpd

# 访问：http://localhost:8080
```

### 运行数据库

```bash
# MySQL
docker run -d \
  --name mysql \
  -e MYSQL_ROOT_PASSWORD=123456 \
  -e MYSQL_DATABASE=myapp \
  -p 3306:3306 \
  -v mysql_data:/var/lib/mysql \
  mysql:8.0

# PostgreSQL
docker run -d \
  --name postgres \
  -e POSTGRES_PASSWORD=123456 \
  -e POSTGRES_DB=myapp \
  -p 5432:5432 \
  -v postgres_data:/var/lib/postgresql/data \
  postgres:15

# MongoDB
docker run -d \
  --name mongodb \
  -e MONGO_INITDB_ROOT_USERNAME=admin \
  -e MONGO_INITDB_ROOT_PASSWORD=123456 \
  -p 27017:27017 \
  -v mongo_data:/data/db \
  mongo:7
```

### 运行 Redis

```bash
docker run -d \
  --name redis \
  -p 6379:6379 \
  -v redis_data:/data \
  redis:7 \
  redis-server --appendonly yes
```

### 运行 Python 应用

```bash
# 运行 Python 脚本
docker run --rm python:3.11 python -c "print('Hello, Docker!')"

# 运行 Python 项目
docker run -d \
  --name myapp \
  -p 8000:8000 \
  -v $(pwd):/app \
  -w /app \
  python:3.11 \
  python app.py
```

### 运行 Node.js 应用

```bash
docker run -d \
  --name nodeapp \
  -p 3000:3000 \
  -v $(pwd):/app \
  -w /app \
  node:18 \
  npm start
```

### 清理系统

```bash
# 清理所有未使用的资源
docker system prune

# 清理所有未使用的资源（包括未使用的镜像）
docker system prune -a

# 清理所有未使用的资源（包括数据卷）
docker system prune -a --volumes

# 查看 Docker 磁盘使用情况
docker system df
```

---

## 故障排查

### 查看容器日志

```bash
# 查看所有日志
docker logs my-nginx

# 实时查看日志
docker logs -f my-nginx

# 查看最近 100 行日志
docker logs --tail 100 my-nginx

# 查看带时间戳的日志
docker logs -t my-nginx
```

### 进入容器调试

```bash
# 进入运行中的容器
docker exec -it my-nginx bash

# 如果容器没有 bash，使用 sh
docker exec -it my-nginx sh

# 以 root 用户进入
docker exec -it --user root my-nginx bash
```

### 检查容器状态

```bash
# 查看容器详细信息
docker inspect my-nginx

# 查看容器资源使用
docker stats my-nginx

# 查看容器进程
docker top my-nginx

# 查看容器端口映射
docker port my-nginx
```

### 常见问题

**问题 1：端口已被占用**

```bash
# 查看端口占用
sudo lsof -i :8080
sudo netstat -tulpn | grep 8080

# 使用其他端口
docker run -d -p 8081:80 nginx
```

**问题 2：容器无法启动**

```bash
# 查看容器退出代码
docker ps -a

# 查看容器日志
docker logs my-nginx

# 以前台模式运行查看错误
docker run nginx
```

**问题 3：权限问题**

```bash
# 检查用户是否在 docker 组
groups

# 添加用户到 docker 组
sudo usermod -aG docker $USER
newgrp docker
```

**问题 4：磁盘空间不足**

```bash
# 查看 Docker 磁盘使用
docker system df

# 清理未使用的资源
docker system prune -a --volumes
```

---

## 常用命令速查

### 镜像操作

| 操作 | 命令 |
|------|------|
| 搜索镜像 | `docker search <镜像名>` |
| 拉取镜像 | `docker pull <镜像名>` |
| 查看镜像 | `docker imadockeges` |
| 删除镜像 | `docker rmi <镜像名>` |
| 构建镜像 | `docker build -t <镜像名> .` |
| 导出镜像 | `docker save -o <文件.tar> <镜像名>` |
| 导入镜像 | `docker load -i <文件.tar>` |

### 容器操作

| 操作 | 命令 |
|------|------|
| 运行容器 | `docker run -d --name <容器名> <镜像名>` |
| 查看容器 | `docker ps -a` |
| 启动容器 | `docker start <容器名>` |
| 停止容器 | `docker stop <容器名>` |
| 重启容器 | `docker restart <容器名>` |
| 删除容器 | `docker rm <容器名>` |
| 进入容器 | `docker exec -it <容器名> bash` |
| 查看日志 | `docker logs -f <容器名>` |
| 查看资源 | `docker stats <容器名>` |
| 复制文件 | `docker cp <容器名>:<路径> <主机路径>` |

### 网络操作

| 操作 | 命令 |
|------|------|
| 查看网络 | `docker network ls` |
| 创建网络 | `docker network create <网络名>` |
| 连接网络 | `docker network connect <网络名> <容器名>` |
| 断开网络 | `docker network disconnect <网络名> <容器名>` |
| 删除网络 | `docker network rm <网络名>` |

### 数据卷操作

| 操作 | 命令 |
|------|------|
| 查看数据卷 | `docker volume ls` |
| 创建数据卷 | `docker volume create <数据卷名>` |
| 删除数据卷 | `docker volume rm <数据卷名>` |
| 查看详情 | `docker volume inspect <数据卷名>` |

### Docker Compose

| 操作 | 命令 |
|------|------|
| 启动服务 | `docker compose up -d` |
| 停止服务 | `docker compose down` |
| 查看状态 | `docker compose ps` |
| 查看日志 | `docker compose logs -f` |
| 构建镜像 | `docker compose build` |
| 重启服务 | `docker compose restart` |

### 系统管理

| 操作 | 命令 |
|------|------|
| 查看信息 | `docker info` |
| 查看版本 | `docker --version` |
| 查看磁盘使用 | `docker system df` |
| 清理系统 | `docker system prune -a` |
| 查看事件 | `docker events` |

---

## 最佳实践

1. **使用数据卷而非绑定挂载**：生产环境推荐使用命名数据卷
2. **使用 .dockerignore**：减少构建上下文大小
3. **多阶段构建**：减小最终镜像大小
4. **使用特定版本标签**：避免使用 `latest` 标签
5. **限制资源使用**：使用 `--memory` 和 `--cpus` 限制资源
6. **健康检查**：使用 `HEALTHCHECK` 指令
7. **不要以 root 运行**：创建非 root 用户运行应用
8. **定期清理**：清理未使用的镜像、容器和网络
9. **使用 Docker Compose**：管理多容器应用
10. **备份数据卷**：定期备份重要数据

---

## 相关资源

- [Docker 官方文档](https://docs.docker.com/)
- [Docker Hub](https://hub.docker.com/)
- [Docker Compose 文档](https://docs.docker.com/compose/)
- [Docker 最佳实践](https://docs.docker.com/develop/dev-best-practices/)

---

**最后更新**: 2025-12-15


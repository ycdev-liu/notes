# Ubuntu 常用命令指南

> Ubuntu / WSL Ubuntu 常用命令和操作指南

## 目录
- [系统管理](#系统管理)
- [软件包管理](#软件包管理)
- [Conda 环境管理](#conda-环境管理)
- [文件和目录操作](#文件和目录操作)
- [文件权限管理](#文件权限管理)
- [进程管理](#进程管理)
- [网络操作](#网络操作)
- [文本处理](#文本处理)
- [系统信息](#系统信息)
- [系统更新与维护](#系统更新与维护)
- [WSL 特定操作](#wsl-特定操作)
- [常用技巧](#常用技巧)

---

## 系统管理

### 系统信息查看

```bash
# 查看 Ubuntu 版本
lsb_release -a

# 查看内核版本
uname -r
uname -a  # 详细信息

# 查看系统位数
getconf LONG_BIT

# 查看主机名
hostname
```

### 用户管理

```bash
# 查看当前用户
whoami

# 查看所有用户
cat /etc/passwd

# 添加用户
sudo adduser username

# 删除用户
sudo deluser username

# 切换用户
su - username

# 以 root 身份执行命令
sudo <命令>

# ubuntu 默认情况下root用户是锁定的，通常不能直接用roo用户登陆
# 通常有两种方式获得 root 权限：使用 sudo 或启用 root 用户
sudo -i
sudo 命令
sudo apt update


# 修改密码
sudo passwd 用户名


# 第二种不推荐

# ubuntu 组的概念

#在 Linux 系统里，每个用户都有一个用户名和一个 UID（用户 ID），同时用户可以属于一个或多个 组（Group），组是用来 管理权限和访问控制的集合。
#可以把它想象成：
# 用户 = 一个具体的人
# 组 = 一群人共享某种权限或资源

# sudo组 adm组 默认自己的组
```



### 服务管理 (systemctl)

```bash


# 列出所有服务
systemctl list-units --type=service

#或者只看正在运行的服务：

systemctl list-units --type=service --state=running
# 查看服务状态
sudo systemctl status <服务名>

# 启动服务
sudo systemctl start <服务名>

# 停止服务
sudo systemctl stop <服务名>

# 重启服务
sudo systemctl restart <服务名>

# 设置开机自启
sudo systemctl enable <服务名>

# 禁用开机自启
sudo systemctl disable <服务名>

# 查看所有运行中的服务
systemctl list-units --type=service --state=running
```

---

## 软件包管理

### APT 包管理器

```bash
# 更新软件包列表
sudo apt update

# 升级所有已安装的包
sudo apt upgrade

# 完整升级（包括内核）
sudo apt full-upgrade

# 安装软件包
sudo apt install <包名>

# 卸载软件包
sudo apt remove <包名>

# 卸载包及其配置文件
sudo apt purge <包名>

# 清理无用的包
sudo apt autoremove

# 搜索软件包
apt search <包名>

# 查看包信息
apt show <包名>
```

### 查看已安装的软件

```bash
# 查看所有已安装的软件
apt list --installed

# 搜索特定软件
apt list --installed | grep <软件名>

# 示例：查看 MySQL 版本
apt list --installed | grep mysql

# 查看特定软件详情
dpkg -l | grep <软件名>

# 查看软件安装位置
whereis <软件名>
which <软件名>
```

### 系统更新

```bash
# 更新软件包列表
sudo apt update

# 查看可升级的包
apt list --upgradable

# 升级所有包（推荐）
sudo apt upgrade

# 完整升级（包括内核，谨慎使用）
sudo apt full-upgrade

# 自动清理（移除不再需要的包）
sudo apt autoremove
sudo apt autoclean
```

---

## Conda 环境管理

### 环境列表与信息

```bash
# 查看所有环境
conda env list
conda info --envs

# 查看当前环境信息
conda info

# 查看当前环境的 Python 版本
python --version

# 查看当前环境安装的包
conda list
pip list
```

### 创建和删除环境

```bash
# 创建新环境（指定 Python 版本）
conda create -n env_name python=3.10

# 创建环境并安装包
conda create -n env_name python=3.10 numpy pandas

# 从 environment.yml 创建环境
conda env create -f environment.yml

# 克隆现有环境
conda create --name new_env --clone old_env

# 删除环境
conda env remove -n env_name
conda remove --name env_name --all
```

### 激活和退出环境

```bash
# 激活环境
conda activate env_name

# 退出当前环境
conda deactivate

# 激活 base 环境
conda activate base
```

### 包管理

```bash
# 安装包（conda）
conda install package_name
conda install numpy pandas matplotlib

# 安装包（pip，在 conda 环境中）
pip install package_name

# 安装指定版本
conda install package_name=1.2.3

# 从特定 channel 安装
conda install -c conda-forge package_name

# 更新包
conda update package_name
conda update --all  # 更新所有包

# 卸载包
conda remove package_name
pip uninstall package_name

# 搜索包
conda search package_name
```

### 导出和共享环境

```bash
# 导出当前环境到 environment.yml
conda env export > environment.yml

# 导出为 requirements.txt（pip 格式）
pip freeze > requirements.txt

# 导出为 conda 格式（只包含 conda 安装的包）
conda env export --from-history > environment.yml

# 从 requirements.txt 安装
pip install -r requirements.txt
```

### 环境清理

```bash
# 清理 conda 缓存
conda clean --all

# 清理 pip 缓存
pip cache purge

# 查看环境占用空间
du -sh ~/miniconda3/envs/*
du -sh ~/anaconda3/envs/*
```

### 常见问题处理

```bash
# 修复损坏的环境
conda update --all

# 重新安装 conda
conda install -n base conda

# 查看 conda 配置
conda config --show

# 添加 conda-forge channel
conda config --add channels conda-forge

# 设置 channel 优先级
conda config --set channel_priority strict
```

### 实用脚本示例

```bash
# 快速切换环境的别名（添加到 ~/.bashrc）
alias conda-vllm='conda activate vllm'
alias conda-base='conda activate base'

# 查看所有环境的 Python 版本
for env in $(conda env list | grep -v '^#' | awk '{print $1}'); do
    echo "=== $env ==="
    conda run -n $env python --version
done
```

---

## 文件和目录操作

### 路径操作

> **重要：**Ubuntu/Linux 中路径分隔符使用正斜杠 `/`，不是 Windows 的反斜杠 `\`

```bash
# 查看当前目录
pwd

# 切换目录（使用正斜杠）
cd /home/user/AI_Study
cd AI_Study/FastAPI  # 相对路径
cd ~  # 切换到用户主目录
cd -  # 切换到上一次的目录
cd ..  # 返回上一级目录

# 列出文件
ls  # 基本列表
ls -l  # 详细信息
ls -la  # 包括隐藏文件
ls -lh  # 人类可读的文件大小
ls -lrt  # 按时间排序
```

### 创建软硬链接



软链接（Symbolic Link / Soft Link）（可以方便python直接引用）
**最常用**，类似于 Windows 的“快捷方式”。它指向的是目标文件的路径。

* **特点**：
    * 可以跨文件系统（跨磁盘分区）。
    * 可以为**目录**创建链接。
    * 如果原始文件被删除，链接将失效（变成“死链接”）。

* **语法**：
    ```bash
    ln -s [源文件或目录的绝对路径] [链接文件的名称]
    ```

* **示例**：
    ```bash
    # 为文件创建软链接
    ln -s /home/user/data.txt  ~/Desktop/data_link

    # 为文件夹创建软链接
    ln -s /var/www/html  ~/my_web_folder
    ```


硬链接（Hard Link）
硬链接是指向文件在磁盘上的物理索引（Inode）。

* **特点**：
    * 不支持跨文件系统（必须在同一分区）。
    * **不能**为目录创建硬链接。
    * 即使删除了原始文件，只要硬链接还在，文件内容就不会丢失。

* **语法**：
    ```bash
    ln [源文件路径] [链接文件名称]
    ```

* **示例**：
    ```bash
    ln /home/user/script.sh  ~/script_backup
    ```



### 目录操作

```bash
# 创建目录
mkdir mydir
mkdir -p parent/child/grandchild  # 递归创建

# 删除空目录
rmdir mydir

# 删除目录及其内容
rm -r mydir  # 递归删除
rm -rf mydir  # 强制删除（谨慎使用）

# 复制目录
cp -r source_dir dest_dir

# 移动/重命名目录
mv old_name new_name
mv mydir /path/to/destination/
```

### 文件操作

```bash
# 创建空文件
touch file.txt

# 复制文件
cp source.txt dest.txt
cp -i source.txt dest.txt  # 覆盖前确认

# 移动/重命名文件
mv old.txt new.txt

# 删除文件
rm file.txt
rm -f file.txt  # 强制删除

# 查看文件内容
cat file.txt  # 显示全部内容
head file.txt  # 显示前 10 行
head -n 20 file.txt  # 显示前 20 行
tail file.txt  # 显示后 10 行
tail -f file.txt  # 实时显示新内容
less file.txt  # 分页查看
more file.txt  # 分页查看

# 编辑文件
nano file.txt  # 简单编辑器 # 操作简单，下方有命令介绍
vim file.txt  # Vim 编辑器
```

### 文件搜索

```bash
# 按名称搜索
find . -name "*.py"
find /home -name "config.json"

# 按类型搜索
find . -type f  # 文件
find . -type d  # 目录

# 按大小搜索
find . -size +10M  # 大于 10MB
find . -size -1M  # 小于 1MB

# 按时间搜索
find . -mtime -7  # 7 天内修改的文件

# 使用 locate （更快）
sudo updatedb  # 更新数据库
locate file.txt
```

---

## 文件权限管理

### 查看权限

```bash
# 查看文件权限
ls -l file.txt
# 输出示例：-rw-r--r-- 1 user group 1024 Oct 16 10:00 file.txt
# 解读：- rw- r-- r--
#       文件类型 所有者 组 其他人
```

### 修改权限 (chmod)

```bash
# 数字方式（rwx = 4+2+1 = 7）
chmod 755 file.sh  # rwxr-xr-x
chmod 644 file.txt  # rw-r--r--
chmod 600 file.txt  # rw-------

# 符号方式
chmod u+x file.sh  # 添加所有者执行权限
chmod g-w file.txt  # 移除组写权限
chmod o+r file.txt  # 添加其他人读权限
chmod a+x file.sh  # 所有人执行权限

# 递归修改目录权限
chmod -R 755 mydir/
```

### 修改所有者 (chown)

```bash
# 修改所有者
sudo chown user file.txt

# 修改所有者和组
sudo chown user:group file.txt

# 递归修改
sudo chown -R user:group mydir/
```

---

## 进程管理

### 查看进程

```bash
# 查看所有进程
ps aux
ps -ef

# 查看特定进程
ps aux | grep python

# 实时监控进程
top
htop  # 需要安装：sudo apt install htop

# 查看进程树
pstree

# 查看进程详情
ps aux | grep <pid>
```

### 终止进程

```bash
# 正常终止
kill <pid>

# 强制终止
kill -9 <pid>

# 按名称终止
killall python
pkill python

# 查找并终止
ps aux | grep python | awk '{print $2}' | xargs kill
```

### 后台运行

```bash
# 在后台运行
python script.py &

# 查看后台任务
jobs

# 将后台任务调到前台
fg %1

# 将前台任务调到后台
# 按 Ctrl+Z 暂停，然后输入
bg

# 使用 nohup （关闭终端后继续运行）
nohup python script.py > output.log 2>&1 &
```

---

## 网络操作

### 网络诊断

```bash
# Ping 测试
ping google.com
ping -c 4 google.com  # 发送 4 次

# 查看网络路由
traceroute google.com

# 查看端口占用
netstat -tulpn
ss -tulpn  # 更现代的命令

# 查看特定端口
sudo lsof -i :3306

# 查看 IP 地址
ip addr
ifconfig  # 老命令，需要安装 net-tools
```

### 下载和请求

```bash
# 使用 wget 下载
wget https://example.com/file.zip
wget -O newname.zip https://example.com/file.zip

# 使用 curl
curl -O https://example.com/file.zip
curl -L https://example.com/redirect  # 跟随重定向

# 发送 HTTP 请求
curl -X GET https://api.example.com/data
curl -X POST -H "Content-Type: application/json" -d '{"key":"value"}' https://api.example.com/data
```

### 设置网络代理


窗口设置环境变量
```
export http_proxy="http://127.0.0.1:7890"
export https_proxy="http://127.0.0.1:7890"
```
### 设置全局环境变量

打开配置文件
```
nano ~/.bashrc
```
最后加上
```
export http_proxy="http://127.0.0.1:7890"
export https_proxy="http://127.0.0.1:7890"
```

配置生效
```
source ~/.bashrc
```
验证
```
curl ifconfig.me
```

## 文本处理

### 搜索文本

```bash
# 在文件中搜索
grep "keyword" file.txt
grep -r "keyword" .  # 递归搜索
grep -i "keyword" file.txt  # 忽略大小写
grep -n "keyword" file.txt  # 显示行号
grep -v "keyword" file.txt  # 反向匹配

# 正则表达式搜索
grep -E "pattern" file.txt
egrep "pattern" file.txt
```

### 文本处理工具

```bash
# 统计行数、字数
wc file.txt
wc -l file.txt  # 只统计行数
wc -w file.txt  # 统计字数

# 排序
sort file.txt
sort -r file.txt  # 逆序
sort -n file.txt  # 数字排序

# 去重
uniq file.txt
sort file.txt | uniq  # 先排序再去重

# 替换文本
sed 's/old/new/' file.txt  # 替换每行第一个
sed 's/old/new/g' file.txt  # 替换所有
sed -i 's/old/new/g' file.txt  # 直接修改文件

# 提取列
awk '{print $1}' file.txt  # 输出第一列
awk -F: '{print $1}' /etc/passwd  # 指定分隔符
```

---

## 系统信息

### 磁盘空间

```bash
# 查看磁盘使用情况
df -h

# 查看目录大小
du -sh *
du -h --max-depth=1

# 查找大文件
du -ah | sort -rh | head -20
```

### 内存使用

```bash
# 查看内存使用
free -h

# 实时监控
top
htop
```

### CPU 信息

```bash
# 查看 CPU 信息
lscpu
cat /proc/cpuinfo

# 查看系统负载
uptime
top
```

---

## 系统更新与维护

### 系统更新

```bash
# 更新软件包列表
sudo apt update

# 查看可升级的包
apt list --upgradable

# 升级所有包
sudo apt upgrade

# 完整升级（包括内核）
sudo apt full-upgrade

# 自动清理
sudo apt autoremove  # 移除不再需要的包
sudo apt autoclean   # 清理下载缓存
```

### 系统维护

```bash
# 查看系统日志
journalctl -xe  # 查看系统错误日志
journalctl -u service_name  # 查看特定服务日志

# 清理系统日志（释放空间）
sudo journalctl --vacuum-time=7d  # 只保留 7 天日志
sudo journalctl --vacuum-size=500M  # 限制日志大小为 500MB

# 清理临时文件
sudo rm -rf /tmp/*
sudo rm -rf /var/tmp/*

# 清理 APT 缓存
sudo apt clean
sudo apt autoclean

# 查找大文件
find / -type f -size +100M 2>/dev/null
du -h --max-depth=1 / | sort -rh | head -20
```

### 磁盘空间管理

```bash
# 查看磁盘使用情况
df -h

# 查看目录大小
du -sh /home/*
du -h --max-depth=1 /home

# 查找占用空间最大的目录
du -h / | sort -rh | head -20

# 清理 conda 缓存（如果使用 conda）
conda clean --all

# 清理 pip 缓存
pip cache purge

# 清理 Docker（如果使用）
docker system prune -a
```

### 系统监控

```bash
# 实时监控系统资源
htop  # 需要安装：sudo apt install htop

# 查看系统负载
uptime

# 查看内存使用
free -h

# 查看 CPU 信息
lscpu

# 查看磁盘 I/O
iostat -x 1  # 需要安装：sudo apt install sysstat

# 查看网络流量
iftop  # 需要安装：sudo apt install iftop
```

---

## WSL 特定操作

### WSL 基本信息

镜像下载
https://cloud-images.ubuntu.com/jammy/20260218/
import 安装

```bash
# 查看 WSL 版本
wsl --version  # 在 Windows PowerShell 中执行

# 查看 WSL 发行版
wsl --list --verbose  # 在 Windows PowerShell 中执行

# 查看当前 WSL 发行版
cat /etc/os-release

# 查看 WSL IP 地址
hostname -I
ip addr show eth0
```

### WSL 与 Windows 文件系统互访

```bash
# 在 WSL 中访问 Windows 文件
cd /mnt/c/Users/YourName  # 访问 C 盘用户目录
cd /mnt/d/Projects       # 访问 D 盘项目目录

# 在 Windows 中访问 WSL 文件
# 路径格式：\\wsl$\Ubuntu\home\username
# 或在文件资源管理器地址栏输入：\\wsl$\Ubuntu
```

### WSL 网络配置

```bash
# 查看 WSL IP 地址
ip addr show eth0
hostname -I

# 查看网络接口
ip link show

# 测试网络连接
ping 8.8.8.8
ping google.com
```

### SSH 服务器配置（用于远程连接）

#### 1. 安装和启动 SSH 服务

```bash
# 更新软件包
sudo apt update

# 安装 SSH 服务器
sudo apt install -y openssh-server

# 启动 SSH 服务
sudo service ssh start

# 设置开机自启（WSL 中可能不适用，需要手动启动）
sudo systemctl enable ssh
```

#### 2. 配置 SSH

```bash
# 编辑 SSH 配置
sudo nano /etc/ssh/sshd_config

# 重要配置项：
# Port 22                    # SSH 端口
# PermitRootLogin yes        # 允许 root 登录（根据需要）
# PasswordAuthentication yes # 允许密码认证
# PubkeyAuthentication yes   # 允许密钥认证

# 重启 SSH 服务
sudo service ssh restart
```

#### 3. 检查 SSH 服务状态

```bash
# 查看 SSH 服务状态
sudo service ssh status

# 查看 SSH 端口监听
ss -lntp | grep ssh
sudo netstat -tulpn | grep ssh

# 测试 SSH 连接（本地）
ssh localhost
```

#### 4. Windows 端口转发配置

在 **管理员 PowerShell** 中执行：

```powershell
# 获取 WSL IP 地址
wsl hostname -I

# 设置端口转发（将 Windows 2222 端口转发到 WSL 22 端口）
netsh interface portproxy add v4tov4 `
    listenaddress=0.0.0.0 `
    listenport=2222 `
    connectaddress=<WSL_IP> `
    connectport=22

# 查看端口转发规则
netsh interface portproxy show all

# 删除端口转发规则
netsh interface portproxy delete v4tov4 listenaddress=0.0.0.0 listenport=2222

# 重置所有端口转发
netsh interface portproxy reset
```

#### 5. Windows 防火墙配置

在 **管理员 PowerShell** 中执行：

```powershell
# 添加防火墙规则（允许 SSH 端口）
New-NetFirewallRule `
    -DisplayName "WSL SSH 2222" `
    -Direction Inbound `
    -Protocol TCP `
    -LocalPort 2222 `
    -Action Allow

# 查看防火墙规则
Get-NetFirewallRule | Where-Object {$_.DisplayName -like "*WSL*"}

# 删除防火墙规则
Remove-NetFirewallRule -DisplayName "WSL SSH 2222"
```

#### 6. 每次开机自动设置端口转发

**方法一：手动快速设置（推荐）**

每次开机后，在管理员 PowerShell 执行：

```powershell
# 获取 WSL IP
$wslIp = (wsl hostname -I).Trim()

# 重置并添加端口转发
netsh interface portproxy reset
netsh interface portproxy add v4tov4 `
    listenaddress=0.0.0.0 `
    listenport=2222 `
    connectaddress=$wslIp `
    connectport=22
```

**方法二：创建启动脚本**

1. 创建 PowerShell 脚本 `setup-wsl-ssh.ps1`：

```powershell
# 获取 WSL IP
$wslIp = (wsl hostname -I).Trim()
Write-Host "WSL IP: $wslIp"

# 重置端口转发
netsh interface portproxy reset

# 添加新的端口转发
netsh interface portproxy add v4tov4 `
    listenaddress=0.0.0.0 `
    listenport=2222 `
    connectaddress=$wslIp `
    connectport=22

Write-Host "Port forwarding configured: Windows:2222 -> WSL:$wslIp:22"
```

2. 将脚本添加到 Windows 任务计划程序，设置开机自动运行。

#### 7. 测试 SSH 连接

```bash
# 在 Windows PowerShell 中测试
ssh root@127.0.0.1 -p 2222

# 或在其他电脑上测试（使用 Windows 主机 IP）
ssh root@<Windows_IP> -p 2222
```

### WSL 性能优化

```bash
# 优化 WSL 2 性能（在 Windows 中创建 .wslconfig）
# 文件位置：C:\Users\YourName\.wslconfig
# 内容示例：
# [wsl2]
# memory=8GB
# processors=4
# swap=2GB
# localhostForwarding=true
```

### WSL 常用命令

```bash
# 在 WSL 中执行 Windows 命令
cmd.exe /c dir  # 执行 Windows dir 命令
powershell.exe -Command "Get-Date"  # 执行 PowerShell 命令

# 在 Windows 中执行 WSL 命令
wsl ls -la  # 在 PowerShell 中执行
wsl python script.py
```

---

## 常用技巧

### 1. 管道 (Pipe) 操作

```bash
# 组合多个命令
cat file.txt | grep "keyword" | wc -l
ps aux | grep python | awk '{print $2}'

# 查找大文件
du -ah | sort -rh | head -10

# 查看端口占用
netstat -tulpn | grep :3306
```

### 2. 命令历史

```bash
# 查看命令历史
history

# 执行历史命令
!100  # 执行第 100 条命令
!!  # 执行上一条命令
!grep  # 执行最近一次 grep 命令

# 搜索历史
Ctrl + R  # 然后输入关键词
```

### 3. 命令别名

```bash
# 创建别名
alias ll='ls -alh'
alias update='sudo apt update && sudo apt upgrade'
alias gs='git status'

# 查看所有别名
alias

# 永久保存别名（添加到 ~/.bashrc）
echo "alias ll='ls -alh'" >> ~/.bashrc
source ~/.bashrc
```

### 4. 输出重定向

```bash
# 输出到文件（覆盖）
command > output.txt

# 追加到文件
command >> output.txt

# 重定向错误输出
command 2> error.log

# 重定向所有输出
command > all.log 2>&1

# 丢弃输出
command > /dev/null 2>&1
```

### 5. 压缩和解压

```bash
# tar.gz 格式
tar -czvf archive.tar.gz directory/  # 压缩
tar -xzvf archive.tar.gz  # 解压

# zip 格式
zip -r archive.zip directory/  # 压缩
unzip archive.zip  # 解压

# tar.bz2 格式
tar -cjvf archive.tar.bz2 directory/  # 压缩
tar -xjvf archive.tar.bz2  # 解压
```

### 6. 环境变量

```bash
# 查看所有环境变量
env
printenv

# 查看特定变量
echo $PATH
echo $HOME
echo $USER

# 临时设置
export MY_VAR="value"

# 永久设置（添加到 ~/.bashrc）
echo 'export MY_VAR="value"' >> ~/.bashrc
source ~/.bashrc
```

### 7. 关闭终端继续跑
```
nohup + &
```
例子
```
nohup ./script.sh &
```
自定义输出路径
```
nohup ./script.sh > my_logs.txt 2>&1 &

```
my_logs.txt：将标准输出（stdout）重定向到该文件。

2>&1：将标准错误（stderr）也重定向到标准输出（即同一个文件）。

&：放入后台。

查看进程
```
ps -ef| grep script.sh
```
停止进程
```
kill -9 <PID>
```

### 8. tmux

基本使用
```
# 创建会话
tmux new -s 会话名
# 查看所有会话
tmux ls

# 进入某个会话
tumx attach -t 会话名

# 杀死会话

tumx kiss-session -t 会话名

# 进入会话杀死会话,进入执行以下命令
exit



```

---

## 快捷键

| 快捷键 | 功能 |
|---------|------|
| `Tab` | 自动补全 |
| `Ctrl + C` | 终止当前命令 |
| `Ctrl + Z` | 暂停当前命令 |
| `Ctrl + D` | 退出当前 Shell |
| `Ctrl + L` | 清屏 |
| `Ctrl + R` | 搜索命令历史 |
| `Ctrl + A` | 跳到行首 |
| `Ctrl + E` | 跳到行尾 |
| `Ctrl + U` | 删除到行首 |
| `Ctrl + K` | 删除到行尾 |
| `↑` / `↓` | 命令历史 |

---

## 常用软件安装

```bash
# 开发工具
sudo apt install build-essential
sudo apt install git
sudo apt install vim
sudo apt install curl wget

# Python 环境
sudo apt install python3 python3-pip
sudo apt install python3-venv

# 数据库
sudo apt install mysql-server
sudo apt install mongodb-org
sudo apt install postgresql

# Node.js
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt install -y nodejs

# Docker
sudo apt install docker.io
sudo systemctl start docker
sudo systemctl enable docker
```

---

## 最佳实践

1. **使用 Tab 补全**：减少输入错误
2. **学会管道操作**：组合多个命令实现复杂功能
3. **定期备份**：重要数据定期备份
4. **使用版本控制**：Git 管理代码
5. **注意权限**：谨慎使用 `sudo` 和 `rm -rf`
6. **查看帮助**：`man <命令>` 或 `<命令> --help`
7. **定期更新系统**：`sudo apt update && sudo apt upgrade`
8. **清理无用文件**：定期运行 `sudo apt autoremove` 和 `conda clean --all`
9. **使用环境管理**：为不同项目创建独立的 conda 环境
10. **记录重要操作**：将常用命令添加到 `~/.bashrc` 作为别名

---

## 相关资源

- [Ubuntu 官方文档](https://ubuntu.com/server/docs)
- [Linux 命令大全](https://www.linuxcool.com/)
- [Linux 命令搜索](https://wangchujiang.com/linux-command/)
- [Ubuntu 中文 Wiki](https://wiki.ubuntu.org.cn/)

---

## 实用脚本集合

### 快速系统检查脚本

```bash
#!/bin/bash
# 保存为 check_system.sh

echo "=== 系统信息 ==="
echo "主机名: $(hostname)"
echo "用户: $(whoami)"
echo "系统版本: $(lsb_release -d | cut -f2)"
echo "内核版本: $(uname -r)"
echo ""

echo "=== 磁盘使用 ==="
df -h | grep -E '^/dev|Filesystem'
echo ""

echo "=== 内存使用 ==="
free -h
echo ""

echo "=== CPU 负载 ==="
uptime
echo ""

echo "=== Conda 环境 ==="
if command -v conda &> /dev/null; then
    conda env list
else
    echo "Conda 未安装"
fi
echo ""

echo "=== 网络 IP ==="
hostname -I
```

使用方法：
```bash
chmod +x check_system.sh
./check_system.sh
```

### 清理脚本

```bash
#!/bin/bash
# 保存为 cleanup.sh

echo "开始清理系统..."

# 清理 APT 缓存
sudo apt autoremove -y
sudo apt autoclean

# 清理 conda 缓存
if command -v conda &> /dev/null; then
    conda clean --all -y
fi

# 清理 pip 缓存
if command -v pip &> /dev/null; then
    pip cache purge
fi

# 清理临时文件
sudo rm -rf /tmp/*
sudo rm -rf /var/tmp/*

# 清理系统日志（保留 7 天）
sudo journalctl --vacuum-time=7d

echo "清理完成！"
```

### 环境导出脚本

```bash
#!/bin/bash
# 保存为 export_envs.sh

BACKUP_DIR="$HOME/conda_env_backups"
mkdir -p "$BACKUP_DIR"

if ! command -v conda &> /dev/null; then
    echo "错误: Conda 未安装"
    exit 1
fi

for env in $(conda env list | grep -v '^#' | awk '{print $1}' | grep -v 'base'); do
    echo "导出环境: $env"
    conda env export -n "$env" > "$BACKUP_DIR/${env}.yml" 2>/dev/null
    conda run -n "$env" pip freeze > "$BACKUP_DIR/${env}_pip.txt" 2>/dev/null
done

echo "所有环境已导出到: $BACKUP_DIR"
```

### WSL SSH 快速设置脚本（PowerShell）

```powershell
# 保存为 setup-wsl-ssh.ps1
# 在管理员 PowerShell 中运行

Write-Host "正在获取 WSL IP 地址..." -ForegroundColor Yellow
$wslIp = (wsl hostname -I).Trim()

if ([string]::IsNullOrEmpty($wslIp)) {
    Write-Host "错误: 无法获取 WSL IP 地址" -ForegroundColor Red
    exit 1
}

Write-Host "WSL IP: $wslIp" -ForegroundColor Green

Write-Host "重置端口转发..." -ForegroundColor Yellow
netsh interface portproxy reset

Write-Host "添加端口转发规则..." -ForegroundColor Yellow
netsh interface portproxy add v4tov4 `
    listenaddress=0.0.0.0 `
    listenport=2222 `
    connectaddress=$wslIp `
    connectport=22

Write-Host "检查防火墙规则..." -ForegroundColor Yellow
$firewallRule = Get-NetFirewallRule -DisplayName "WSL SSH 2222" -ErrorAction SilentlyContinue

if (-not $firewallRule) {
    Write-Host "添加防火墙规则..." -ForegroundColor Yellow
    New-NetFirewallRule `
        -DisplayName "WSL SSH 2222" `
        -Direction Inbound `
        -Protocol TCP `
        -LocalPort 2222 `
        -Action Allow | Out-Null
}

Write-Host "`n✅ 配置完成！" -ForegroundColor Green
Write-Host "SSH 连接命令: ssh root@127.0.0.1 -p 2222" -ForegroundColor Cyan
```

---


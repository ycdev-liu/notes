

# huggingface-cli(命令行工具)


```
--bash
# 当下载收到限制时
huggingface-cli login
# 执行后会提示输入 Token（在 HF 官网 Settings -> Access Tokens 获取）

# 下载模型 支持断点续传

huggingface-cli download lerobot/pi0_base --local-dir /home/ksas/models/pi0_base

# 只下载特定文件
huggingface-cli download bert-base-uncased config.json

# 查看本地缓存了哪些模型，占用了多少空间
huggingface-cli scan-cache

# 交互式删除不需要的旧版本模型
huggingface-cli delete-cache

```
python用法

```
from huggingface_hub import snapshot_download

path = snapshot_download(
    repo_id="lerobot/pi0_base",
    local_dir="/home/ksas/models/pi0_base",
    revision="main",          # 指定分支，默认 main
    max_workers=8,            # 2026版支持多线程并行下载
    endpoint="https://hf-mirror.com"  # 国内加速点
)
```

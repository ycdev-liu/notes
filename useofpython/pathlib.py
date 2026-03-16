# pathlib包的用例学习

from pathlib import Path

# 获取当前路径
current_path = Path.cwd()
print(f"当前路径: {current_path}")
# 列出当前路径下的所有文件和文件夹
print("当前路径下的文件和文件夹:")
for item in current_path.iterdir():
    print(f"  {item.name}")
# 创建一个新的目录
new_directory = current_path / "new_folder" 
print(f"准备创建新目录: {new_directory}")
new_directory.mkdir(exist_ok=True)
print(f"新目录已创建: {new_directory}")
# 删除刚才创建的目录
new_directory.rmdir()
print(f"目录已删除: {new_directory}")
# 获取文件的绝对路径
file_name = "example.txt"
absolute_path = (current_path / file_name).resolve()
print(f"文件的绝对路径: {absolute_path}")
# 判断文件是否存在
file_exists = (current_path / file_name).exists()
print(f"文件 {file_name} 是否存在: {file_exists}")
# 获取文件的大小
if file_exists:
    file_size = (current_path / file_name).stat().st_size
    print(f"文件 {file_name} 的大小: {file_size} 字节")
# 获取系统平台
platform = Path().anchor
print(f"系统平台: {platform}")
# 获取当前用户的主目录
home_directory = Path.home()
print(f"当前用户的主目录: {home_directory}")

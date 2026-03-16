# python os 包的使用示例

import os
# 获取当前工作目录
current_directory = os.getcwd()
print(f"当前工作目录: {current_directory}")
# 列出当前目录下的所有文件和文件夹
files_and_folders = os.listdir(current_directory)
print("当前目录下的文件和文件夹:")
for item in files_and_folders:
    print(f"  {item}")
# 创建一个新的目录
new_directory = os.path.join(current_directory, "new_folder")
print(f"准备创建新目录: {new_directory}")
os.makedirs(new_directory, exist_ok=True)
print(f"新目录已创建: {new_directory}") 
# 删除刚才创建的目录
os.rmdir(new_directory)
print(f"目录已删除: {new_directory}")
# 获取系统平台
platform = os.name
print(f"系统平台: {platform}")
# 获取当前用户的主目录
home_directory = os.path.expanduser('~')
print(f"当前用户的主目录: {home_directory}")
# 获取文件的绝对路径
file_name = "example.txt"
absolute_path = os.path.abspath(file_name)
print(f"文件的绝对路径: {absolute_path}")
# 判断文件是否存在
file_exists = os.path.exists(file_name)
print(f"文件 {file_name} 是否存在: {file_exists}")
# 获取文件的大小
if file_exists:
    file_size = os.path.getsize(file_name)
    print(f"文件 {file_name} 的大小: {file_size} 字节")
# 设置环境变量 MY_VARIABLE
os.environ['MY_VARIABLE'] = 'Hello, World!'
print(f"环境变量 MY_VARIABLE: {os.getenv('MY_VARIABLE')}")
# 获取环境变量
path_variable = os.getenv('PATH')
print(f"环境变量 PATH: {path_variable}")
# 获取进程
import os
print(os.getpid)

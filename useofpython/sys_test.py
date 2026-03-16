# sys 包的学习

import sys
print(sys.version)  # 输出Python的版本信息
print(sys.platform)  # 输出当前操作系统平台
print(sys.executable)  # 输出Python解释器的路径
print(sys.path)  # 输出模块搜索路径列表
# 添加一个新的路径到模块搜索路径列表
new_path = "/path/to/your/module"
sys.path.append(new_path)
print(f"新的模块搜索路径列表: {sys.path}")
# 获取命令行参数
print(f"命令行参数: {sys.argv}")
# 获取系统的最大递归深度
print(f"系统的最大递归深度: {sys.getrecursionlimit()}")
# 设置系统的最大递归深度
sys.setrecursionlimit(2000)
print(f"新的系统最大递归深度: {sys.getrecursionlimit()}")
# 获取系统的默认编码
print(f"系统的默认编码: {sys.getdefaultencoding()}")
# 查看标准库
print("标准库模块列表:")
for module in sys.builtin_module_names:
    print(f"  {module}")    
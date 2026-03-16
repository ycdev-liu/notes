# enum 使用

from enum import Enum,auto,StrEnum


# 枚举可以让代码可读性更强，避免使用魔法数字或字符串来表示特定的状态或选项。


# 定义一个枚举类
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
# 使用枚举成员
print(Color.RED)  # 输出Color.RED


# 枚举成员的值
print(Color.RED.value)  # 输出1
# 枚举成员的名称
print(Color.RED.name)  # 输出'RED'
# 枚举成员的类型
print(type(Color.RED))  # 输出<enum 'Color'>

# 使用auto自动分配值
class AutoColor(Enum):
    RED = auto()
    GREEN = auto()
    BLUE = auto()
print(AutoColor.RED.value)  # 输出1
print(AutoColor.GREEN.value)  # 输出2
print(AutoColor.BLUE.value)  # 输出3


# 定义一个字符串枚举类
class StrColor(StrEnum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'
print(StrColor.RED)  # 输出StrColor.RED
print(StrColor.RED.value)  # 输出'red'
print(StrColor.RED.name)  # 输出'RED'

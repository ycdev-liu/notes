# 学习typing模块的使用
from typing import List, Dict, Tuple, Set, Optional,Annotated, Any,TypeAlias,Literal


# 使用类型注解
def process_items(items: List[str]) -> Dict[str, int]:
    return {item: len(item) for item in items}

# 使用可选类型
def get_user_name(user_id: int) -> Optional[str]:
    # 模拟从数据库获取用户名称
    if user_id == 1:
        return "Alice"
    return None

# 使用Annotated类型
def calculate_area(radius: Annotated[float, "圆的半径"]) -> float:
    import math
    return math.pi * radius ** 2


# 使用TypeAlias定义类型别名
UserID: TypeAlias = int
def get_user_info(user_id: UserID) -> Dict[str, Any]:
    # 模拟从数据库获取用户信息
    if user_id == 1:
        return {"name": "Alice", "age": 30}
    return {"name": "Unknown", "age": 0}

# 使用Literal定义字面量类型
# 定义一个函数，接受一个状态参数，状态只能是'active'、'inactive'或'pending'
# 这可以帮助我们在调用函数时提供更明确的类型提示，并且在传递无效状态时会引发类型检查错误。
def set_status(status: Literal['active', 'inactive', 'pending']) -> None:
    print(f"Status set to: {status}")

# 示例调用
items = ["apple", "banana", "cherry"]
result = process_items(items)
print(result)

user_name = get_user_name(1)
print(user_name)

area = calculate_area(5.0)
print(area)

user_info = get_user_info(1)
print(user_info)

set_status('active')
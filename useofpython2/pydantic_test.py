# pydantic的使用
from pydantic import BaseModel, ValidationError


# Pydantic 是一个 数据验证和设置管理库，基于 Python 的 类型注解。它可以：
# 自动校验数据类型
# 提供默认值和可选字段
# 自动转换类型（比如把字符串 "123" 转为整数 123）
# 在 FastAPI、数据处理、配置管理中非常常用



from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    age: str
    is_active: bool = True  # 默认值为 True

# 创建一个用户实例
try:
    user = User(id=1, name="Alice", age="30")
    print(user)
except ValidationError as e:
    print(e)


# 数据类型转换
user2= User(id="2", name="Bob", age="25", is_active=False)
print(user2)


from typing import Literal,Optional
from pydantic import BaseModel


class Task(BaseModel):
    id: int
    title: str
    status: Literal['pending', 'in_progress', 'completed']  # 限定状态只能是这三个值
    description: Optional[str] = None  # 可选字段，默认为 None

# 创建一个任务实例
try:
    task = Task(id=1, title="Write code", status="in_progress")
except ValidationError as e:
    print(e)
print(task)


# 嵌套结构
class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    age: str
    is_active: bool = True
    address: Address  # 嵌套的 Address 实例
p = User(id=1, name="Alice", age="30", address={"street": "123 Main St", "city": "Anytown", "zip_code": "12345"})
print(p)

from pydantic import BaseModel,field_validator


class Product(BaseModel):
    name: str
    price: float

    # 字段验证器，确保价格必须是正数
    @field_validator('price')
    def price_must_be_positive(cls, value):
        if value <= 0:
            raise ValueError('价格必须是正数')
        return value

from pydantic import BaseModel,model_validator

class User(BaseModel):
   passward: str
   confirm_password: str
   @model_validator(mode='after')
   def check_passwords(self):
       if self.passward != self.confirm_password:
           raise ValueError('密码和确认密码必须匹配')
       return self

user = User(passward='secret', confirm_password='secret')
print(user)

from pydantic import SerializeAsAny

from typing import Any

class Config(BaseModel):
    data: SerializeAsAny[Any]

m = Config(data={"key": "value"})
print(m.model_dump())

# SerializeAsAny 允许我们在 Pydantic 模型中定义一个字段，该字段可以接受任何类型的数据，并且在序列化时保持原样。这对于需要存储或传输任意数据结构的场景非常有用，比如配置文件、日志记录等。


# 一个典型场景

from pydantic import BaseModel

class User(BaseModel):
    name: str

class Adress(User):
    city:str
    zipcode:str

admin = Adress(name="Alice", city="Anytown", zipcode="12345")

class Wrapper(BaseModel):
    user: SerializeAsAny[User]

w = Wrapper(user=admin)
print(w.model_dump())

# 序列化时按照真实类型序列化，而不是按照字段声明类型。


class Adress(BaseModel):
    city:str
    zipcode:str

class Person(BaseModel):
    name:str
    age:int
    address:Adress

p = Person(name="Alice", age=30, address={"city": "Anytown", "zipcode": "12345"})

print(p.model_dump())



from typing import Literal,Optional

class Task(BaseModel):
    id: int
    title: str
    status: Literal['pending', 'in_progress', 'completed']  # 限定状态只能是这三个值
    description: Optional[str] = None  # 可选字段，默认为 None



# computed fields 计算字段
from pydantic import BaseModel, computed_field

class Rectangle(BaseModel):
    width: float
    height: float

    @computed_field
    @property
    def area(self) -> float:
        return self.width * self.height
    

rect = Rectangle(width=5.0, height=3.0)
print(rect.area)  # 输出15.0


# model_config 配置模型行为
from pydantic import BaseModel, ConfigDict

class User(BaseModel):
    name: str
    age: int

    model_config = ConfigDict(extra="forbid")  # 禁止额外字段



# User(id=1, name="Alice", age=20)  # 会引发验证错误，因为 id 字段未定义且 extra="forbid" 禁止额外字段


class User(BaseModel):
    name: str
    age: int

    model_config = ConfigDict(extra="ignore")  # 禁止额外字段



User(id=1, name="Alice", age=20)  # 会引发验证错误，因为 id 字段未定义且 extra="forbid" 禁止额外字段



# extra 选项：
# 值	含义
# allow	允许额外字段
# ignore	忽略
# forbid	报错

# 序列化
# 把机器拆成零件装箱运输
# Python对象
#    ↓
# 序列化
#    ↓
# JSON / 字符串 / bytes
# 反序列化就是：
# JSON
#   ↓
# 反序列化
#   ↓
# 重新变成对象

""""
| 方法                  | 作用         | 返回类型        |
| ------------------- | ---------- | ----------- |
| `model_dump()`      | 模型 → dict  | Python dict |
| `model_dump_json()` | 模型 → JSON  | str         |
| `SerializeAsAny`    | 序列化时保留真实类型 | 高级特性        |

"""

# OOP python 学习



# | 方法            | 作用         |
# | ------------- | ---------- |
# | `__init__`    | 构造函数       |
# | `__str__`     | print对象时调用 |
# | `__repr__`    | 调试输出       |
# | `__len__`     | len()      |
# | `__add__`     | + 运算       |
# | `__getitem__` | 索引访问       |


# 魔术方法
class MyClass:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"MyClass with value: {self.value}"

    def __add__(self, other):
        if isinstance(other, MyClass):
            return MyClass(self.value + other.value)
        return NotImplemented
    
    def __getitem__(self, index):
        if index == 0:
            return self.value
        raise IndexError("Index out of range")
    def __len__(self):
        return len(str(self.value))


# 运算符重载
class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
v1 = Vector(1,2)
v2 = Vector(3,4)

v3 = v1 + v2
print(v3.x, v3.y)  # 输出: 4 6


# 属性管理 property

class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value


p = Person("zhangsan")

p.age = 20
print(p.age)


# 多继承
class A:
    def method_a(self):
        print("Method A")
class B:
    def method_b(self):
        print("Method B")
class C(A, B):
    pass

c=C()
# MRO 方法解析顺序
print(C.mro())  # 输出: [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]

# super()函数
class Parent:
    def __init__(self, name):
        self.name = name
        print(f"Parent initialized with name: {self.name}")
class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # 调用父类的构造函数
        self.age = age
        print(f"Child initialized with name: {self.name} and age: {self.age}")



d = Child("liubei",2)


# 抽象类
from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass



# 子类必须继承
class Dog(Animal):
    def speak(self):
        print("汪汪")



# 鸭子类型

class Dog:
    def speak(self):
        print("汪汪")
class cat:
    def speak(self):
        print("喵")



def make_sound(animal):
    animal,speak()

from dataclasses import dataclass


# Python 3.7+ 推荐写法。
# 自动生成：
# __init__
# __repr__
# __eq__

@dataclass
class Person:
    name:str
    age:int

p = Person("Tom",20)
print(p)

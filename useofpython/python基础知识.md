# 一、Python 基础（送命必问）

## 1️⃣ Python 是强类型还是弱类型？动态还是静态？

- **强类型 + 动态语言**
- 变量类型在运行时确定
- 不会自动隐式类型转换（如 `"1" + 1` 报错）

---

## 2️⃣ 可变对象 vs 不可变对象

- 不可变：`int、float、str、tuple`
- 可变：`list、dict、set`
- 不可变对象修改 → 产生新对象
    
    ---
    

## 3️⃣ list / tuple / set / dict 区别

| 类型 | 是否有序 | 是否可变 | 是否可重复 |
| --- | --- | --- | --- |
| list | ✅ | ✅ | ✅ |
| tuple | ✅ | ❌ | ✅ |
| set | ❌ | ✅ | ❌ |
| dict | 3.7+ 有序 | key 不可变 | key 不重复 |

---

## 4️⃣ 为什么 dict 查找是 O(1)？

- 哈希表
- key → hash → slot
- 冲突用开放寻址

---

## 5️⃣ Python 中 is 和 == 的区别

- `is`：对象 id 是否相同
- `==`：值是否相等
    
    ---
    

# 二、函数 & 作用域（高频）

## 6️⃣ Python 参数传递是值传递还是引用传递？

👉 **对象引用传递**

- 不可变对象：表现得像值传递
- 可变对象：函数内修改会影响外部

---

## 7️⃣ 默认参数为什么不能用可变对象？

```python
deff(x, arr=[]):
    arr.append(x)

```

- 默认参数在**函数定义阶段就创建**
- 多次调用共享同一个对象

---

## 8️⃣ *args 和 **kwargs 区别

- `args`：位置参数（tuple）
- `*kwargs`：关键字参数（dict）

---

## 9️⃣ 闭包是什么？

- 内层函数引用外层函数变量
- 常用于装饰器

---

# 三、装饰器（面试官最爱）

## 🔟 装饰器的执行顺序

### 在不改变原有功能的基础上，增加新的功能，---接受函数并返回新的函数。


### 用途

日志记录
权限验证
缓存
计时
web路由



```python
@a
@b
deff():pass

```

等价于：

```python
f = a(b(f))

```

---

## 1️⃣1️⃣ 装饰器为什么要用 functools.wraps？

- 保留原函数：
    - `__name__`
    - `__doc__`

---

# 四、迭代器 & 生成器

## 1️⃣2️⃣ 生成器有什么好处？

- 惰性计算
- 节省内存
- 适合大数据流

---

## 1️⃣3️⃣ yield 和 return 区别

- `yield`：返回值 + 保存状态
- `return`：结束函数

---

# 五、异常处理（必考）

## 1️⃣4️⃣ try / except / else / finally 执行顺序

- 无异常 → try → else → finally
- 有异常 → try → except → finally

---

## 1️⃣5️⃣ raise 的作用

- 主动抛异常
- 自定义异常

---

# 六、面向对象（Python OOP）

## 1️⃣6️⃣ @staticmethod vs @classmethod

| 类型 | 参数 | 使用场景 |
| --- | --- | --- |
| staticmethod | 无 self/cls | 工具函数 |
| classmethod | cls | 工厂方法 |

---

## 1️⃣7️⃣ Python 中私有变量是怎么实现的？

- `__name` → 名字改写（name mangling）
- 不是绝对私有

---

## 1️⃣8️⃣ 多继承的 MRO 顺序

- C3 线性化
- 使用 `super()`

---

# 七、内存 & GC（中高级）

## 1️⃣9️⃣ Python 内存管理机制

- 引用计数
- 标记-清除
- 分代回收

---

## 2️⃣0️⃣ 什么是循环引用？如何解决？

- 对象相互引用，引用计数不为 0
- 由 GC 标记-清除解决

---

# 八、并发基础（必问）

## 2️⃣1️⃣ GIL 是什么？

- 全局解释器锁
- 保证线程安全
- 限制多线程 CPU 并行

**Python 的 GIL（Global Interpreter Lock，全局解释器锁）** 是理解 Python 并发/并行性能的一个关键点，尤其是做工程或系统设计时。

---

## 1️⃣ 什么是 GIL？

**GIL 是一个互斥锁**，保证 **同一时刻只有一个线程在执行 Python 字节码**。

> 即使你的机器有很多 CPU 核心，一个 Python 进程里的多个线程也无法真正并行执行 Python 代码。
> 

主要存在于 **CPython（官方实现）** 中。

---

## 2️⃣ 为什么 Python 要有 GIL？
**简化内存管理，提高单线程性能**

### 🔹 1. 简化垃圾回收

- CPython 使用 **引用计数** 管理内存
- 多线程同时修改引用计数 → 需要大量细粒度锁
- GIL 用一个大锁，避免复杂的并发内存问题

### 🔹 2. 提高单线程效率

- 没有 GIL → 每个对象都要加锁
- GIL 在 **单线程 / I/O 场景**下反而更快

---

## 3️⃣ GIL 带来的影响

### ❌ 对 CPU 密集型任务

```python
# CPU 密集
def calc():
    x = 0
    for i in range(10**7):
        x += i

```

- 多线程 ❌ **不会变快**
- 甚至可能更慢（线程切换开销）

### ✅ 对 I/O 密集型任务

```python
# I/O 密集
def download():
    requests.get(url)

```

- I/O 时会 **释放 GIL**
- 多线程 ✔️ 明显提速

---

## 4️⃣ GIL 什么时候会被释放？

### ✔️ 自动释放

- I/O 操作（文件、网络、sleep）
- 阻塞系统调用

### ✔️ 手动释放（C 扩展）

```c
Py_BEGIN_ALLOW_THREADS
// 耗时 C 代码
Py_END_ALLOW_THREADS

```

👉 这也是 **NumPy / PyTorch 能多核加速的原因**（底层是 C/C++）。

---

## 5️⃣ 多线程 vs 多进程

| 场景 | 推荐方案 |
| --- | --- |
| I/O 密集 | `threading` |
| CPU 密集 | `multiprocessing` |
| 深度学习 | PyTorch / NumPy（释放 GIL） |
| 高并发服务 | async / event loop |

### 多进程示例

```python
from multiprocessing import Pool

def work(x):
    return x * x

if __name__ == "__main__":
    with Pool(4) as p:
        print(p.map(work, range(10)))

```

---

## 6️⃣ GIL 与 async/await

- `asyncio` **不是多线程**
- 是 **单线程 + 协程调度**
- 本质：避免线程竞争，而不是绕过 GIL

👉 非常适合：

- Web 服务
- 爬虫
- 高并发 I/O

---

## 7️⃣ GIL 是否会被移除？

### 🔥 重要进展

- **Python 3.13+**：PEP 703（No-GIL）实验性支持
- 未来目标：**可选 GIL**
- 代价：单线程性能下降、生态适配成本高

👉 **短期内 GIL 仍然是主流现实**

---

## 8️⃣ 一句话总结

> GIL 不是“Python 慢”的根本原因，而是 CPython 的设计取舍。
> 
- I/O 并发：用线程 / async
- CPU 并行：用多进程 / C 扩展
- 工程上：**绕过 GIL，而不是对抗 GIL**

---

---

## 2️⃣2️⃣ 什么时候用多线程？什么时候用多进程？

- IO 密集 → 多线程 / 协程
- CPU 密集 → 多进程

---

# 九、字符串 & 编码

## 2️⃣3️⃣ Python 中 str 是什么编码？

- Python 3：Unicode
- UTF-8 是存储/传输格式

---

## 2️⃣4️⃣ join 和 + 拼接字符串区别

- `join` 更高效（一次分配内存）

---

# 十、常见坑题（极高频）

## 2️⃣5️⃣ 下面代码输出什么？

```python
a = [1,2,3]
b = a
b.append(4)
print(a)

```

👉 `[1, 2, 3, 4]`

---

## 2️⃣6️⃣ 下面代码输出？

```python
for iinrange(3):
deff():
print(i)
f()

```




你这段其实是在总结 **Python 运行脚本和导入模块时常见的坑**。我帮你整理成更清晰的笔记，并补充一点解释，方便以后复习。👇

---

# Python 运行文件与模块导入注意事项

## 1️⃣ 闭包晚绑定（Late Binding）

Python 的闭包在循环中容易出现 **晚绑定问题**。

示例：

```python
funcs = []
for i in range(3):
    funcs.append(lambda: i)

for f in funcs:
    print(f())
```

输出：

```
2
2
2
```

原因：
lambda 没有保存当时的 `i`，而是 **在调用时才查找变量**。

解决办法：

```python
funcs = []
for i in range(3):
    funcs.append(lambda i=i: i)

for f in funcs:
    print(f())
```

输出：

```
0
1
2
```

---

# 2️⃣ Python 包引用注意事项

在 Python 项目中，**导入方式很重要**。

例如项目结构：

```
project/
│
├─ main.py
└─ app/
   ├─ __init__.py
   ├─ config.py
   └─ request.py
```

---

## 推荐方式：绝对导入（最稳健）

不要使用很多 `.` 的相对导入，而是 **从项目根目录开始导入**。

例如在 `request.py` 中：

```python
from app.config import settings
```

优点：

* 可读性高
* 不容易出错
* IDE 解析更好
* 适合大型项目

---

## 不推荐：复杂相对导入

例如：

```python
from ..config import settings
```

问题：

* 层级深容易错
* 移动文件会坏
* IDE 自动补全差

---

# 3️⃣ 直接运行 Python 文件的坑

如果你直接运行：

```bash
python main.py
```

那么 **main.py 不能使用相对导入**。

例如：

```python
from .app.config import settings
```

会报错：

```
ImportError: attempted relative import with no known parent package
```

原因：

当直接运行 `.py` 文件时，
Python 不把它当作 **包的一部分**。

---

# 4️⃣ 推荐运行方式（大型项目）

使用 `-m` 方式运行模块：

```bash
python -m app.main
```

这样 Python 会把项目当成包结构处理。

---

# 5️⃣ 最推荐的实践总结

✔ 使用 **绝对导入**

```python
from app.config import settings
```

✔ 项目结构清晰

```
project/
    main.py
    app/
        config.py
        request.py
```

✔ 尽量使用模块方式运行

```bash
python -m app.main
```

---

💡 一句话总结：

**Python 项目里：尽量用绝对导入 + 模块运行方式，避免相对导入带来的问题。**


# Python 导入机制完整笔记

## 1️⃣ Python 是如何找到模块的（sys.path）

当你写：

```python
import app.config
```

Python 会按顺序在 **sys.path** 里面查找模块。

查找顺序：

1. 当前运行脚本的目录
2. 环境变量 `PYTHONPATH`
3. Python 安装目录里的库
4. site-packages

查看：

```python
import sys
print(sys.path)
```

示例输出：

```
[
'/project',
'/usr/lib/python3.10',
'/usr/lib/python3.10/site-packages'
]
```

所以只要 **项目根目录在 sys.path 里**，就可以：

```python
from app.config import settings
```

---

# 2️⃣ `__name__ == "__main__"` 的作用

每个 Python 文件都有一个 `__name__`。

### 被直接运行

```bash
python main.py
```

`main.py`

```python
print(__name__)
```

输出：

```
__main__
```

---

### 被导入

```python
import main
```

输出：

```
main
```

---

### 常见写法

```python
def main():
    print("run program")

if __name__ == "__main__":
    main()
```

作用：

* 只有 **直接运行** 才执行
* 被导入不会执行

---

# 3️⃣ 绝对导入 vs 相对导入

## 绝对导入（推荐）

```python
from app.config import settings
```

优点：

* 清晰
* IDE支持好
* 不会乱

这也是
FastAPI
Django
官方推荐方式。

---

## 相对导入

```python
from .config import settings
```

或者

```python
from ..config import settings
```

点的含义：

```
.  当前目录
.. 上级目录
... 上两级
```

问题：

* 层级深容易乱
* 重构代码容易坏

---

# 4️⃣ 为什么 `python main.py` 会导入失败

项目结构：

```
project/
│
├─ main.py
└─ app/
   ├─ __init__.py
   ├─ config.py
   └─ request.py
```

如果 `request.py` 写：

```python
from .config import settings
```

然后运行：

```
python request.py
```

会报错：

```
ImportError: attempted relative import with no known parent package
```

原因：

Python 不知道 `request.py` 属于 `app` 包。

---

# 5️⃣ 正确运行方式（重要）

推荐使用 **模块运行**：

```bash
python -m app.request
```

Python 会认为：

```
app.request
属于 package
```

相对导入就能正常工作。

---

# 6️⃣ Python 项目最佳结构

推荐结构：

```
project/
│
├─ main.py
├─ requirements.txt
│
└─ app/
   ├─ __init__.py
   ├─ config.py
   ├─ request.py
   └─ service.py
```

导入方式：

```python
from app.config import settings
from app.service import UserService
```

---

# 7️⃣ 为什么大项目都用绝对导入

原因：

1️⃣ 重构安全
2️⃣ IDE 自动补全好
3️⃣ 路径清晰
4️⃣ 不依赖运行位置

例如：

* FastAPI
* Django
* Flask

源码全部是 **绝对导入**。

---

# 8️⃣ Python 导入常见坑（面试高频）

### 坑1 重复导入

```python
import module
import module
```

Python **只加载一次**，因为有缓存：

```python
sys.modules
```

---

### 坑2 循环导入

```
a.py -> import b
b.py -> import a
```

会报错：

```
ImportError: circular import
```

解决：

* 拆模块
* 延迟导入

例如：

```python
def func():
    from b import test
```

---

# 9️⃣ 一条开发黄金规则

Python 项目记住一句话：

**始终使用绝对导入，从项目根目录开始。**

例如：

```python
from app.config import settings
```

而不是：

```
from ..config import settings
```

---

✅ **最终推荐运行方式**

```bash
python -m app.main
```

而不是：

```
python main.py
```

---


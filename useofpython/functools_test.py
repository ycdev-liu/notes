
# functools 基本使用
# functools模块提供了高阶函数和可调用对象的工具，常用于函数式编程和性能优化。
# 1. lru_cache装饰器：用于缓存函数的结果，避免重复计算，提高性能。
# 2. cache装饰器：Python 3.9引入的简化版lru_cache，适用于不需要限制缓存大小的情况。

from functools import lru_cache,cache

# 使用lru_cache装饰器来缓存函数结果
@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))  # 输出55

# 使用cache装饰器来缓存函数结果
@cache
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
print(factorial(5))  # 输出120

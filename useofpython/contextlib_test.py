# contextlib的使用
from contextlib import asynccontextmanager
from contextlib import contextmanager, asynccontextmanager


# 定义一个上下文管理器
@contextmanager
def my_context():
    print("Entering the context")
    yield
    print("Exiting the context")

with my_context():
    print("Inside the context")

# 定义一个异步上下文管理器
@asynccontextmanager
async def my_async_context():
    print("Entering the async context")
    yield
    print("Exiting the async context")\
    
import asyncio
async def main():
    async with my_async_context():
        print("Inside the async context")
asyncio.run(main())




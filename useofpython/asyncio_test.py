# asyncio 学习
import asyncio

# asyncio 是 Python 提供的 异步编程框架，主要用于：
# 协程（async / await）
# 事件循环（event loop）
# 高并发 IO（网络请求、爬虫、服务器等）
# 它特别适合 IO 密集型任务，例如：
# 网络爬虫
# Web 服务
# 高并发 API 请求
# websocket 通信

async def main():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

asyncio.run(main())


# asyncio 的事件循环机制允许我们同时处理多个任务，而不需要等待每个任务完成。
# 这使得 asyncio 非常适合处理大量的网络请求或其他 IO 操作，而不会阻塞程序的执行。

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    print("Start tasks")
    # 并发执行两个协程
    task1 = asyncio.create_task(say_after(2, "Hello"))
    task2 = asyncio.create_task(say_after(1, "World"))

    print("Waiting for tasks to finish")
    await task1
    await task2

# asyncio.run(main())


import asyncio

async def fetch_data(n):
    print(f"Start fetching {n}")
    await asyncio.sleep(n)
    print(f"Done fetching {n}")
    return f"Data {n}"

async def main():
    # 并发执行三个协程，并收集返回值
    results = await asyncio.gather(
        fetch_data(3),
        fetch_data(1),
        fetch_data(2)
    )
    print("Results:", results)

# asyncio.run(main())
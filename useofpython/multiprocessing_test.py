# multiprocessing 学习


# multiprocessing 用于python 多进程并发的标准模块

# 特点
"""
每一个进程都有自己独立的python解释器
每一个进程都有自己的GIL
可以真正利用多核CPU
"""

# 基本使用
"""
CPU 密集型任务
数据计算
并行处理
机器学习
"""


from multiprocessing import Process
import os

def task():
    print("process_id",os.getpid())

p1= Process(target=task)
p2=Process(target=task)

p1.start()
p2.start()

p1.join()
p2.join()



from multiprocessing import Pool

def square(x):
    return x * x

with Pool(4) as p:
    result = p.map(square, [1,2,3,4,5])

print(result)


"""
| 特性      | multiprocessing | threading |
| ------- | --------------- | --------- |
| 并发单位    | 进程              | 线程        |
| 是否受 GIL | ❌ 不受            | ✅ 受       |
| 内存      | 独立              | 共享        |
| 开销      | 较大              | 较小        |
| 适合任务    | CPU密集           | IO密集      |


"""
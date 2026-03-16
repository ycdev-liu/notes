# collections模块的学习
from collections import Counter, defaultdict, deque,namedtuple,OrderedDict

# Counter的使用
counter = Counter('hello world')
print(counter)  # 输出Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
# 获取元素的计数
print(counter['l'])  # 输出3
# 获取最常见的元素
most_common = counter.most_common(2)
print(most_common)  # 输出[('l', 3), ('o', 2)]
# 更新计数器
counter.update('hello')
print(counter)  # 输出Counter({'l': 6, 'o': 4, 'h': 2, 'e': 2, ' ': 2, 'w': 1, 'r': 1, 'd': 1})


# d = {}
# d["a"] += 1  # 这会抛出KeyError，因为键"a"不存在


# defaultdict的使用（自动获取默认值）
default_dict = defaultdict(int)
default_dict['a'] += 1
default_dict['b'] += 2
# 输出defaultdict(<class 'int'>, {'a': 1, 'b': 2})
print(default_dict) 


# namedtuple的使用
Point = namedtuple('point', ['x', 'y'])
point = Point(1, 2)
print(point)  # 输出Point(x=1, y=2)
print(point.x)  # 输出1
print(point.y)  # 输出2


# 优点：
# 比 tuple 更清晰
# 不可变
# 比 class 更轻量

# deque的使用
queue = deque([1, 2, 3])
queue.append(4)  # 在右侧添加元素
queue.appendleft(0)  # 在左侧添加元素
print(queue)  # 输出deque([0, 1, 2, 3, 4])
queue.pop()  # 从右侧移除元素


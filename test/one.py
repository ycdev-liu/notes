# class A:
#     @property
#     def age(self):
#         return self._age

#     @age.setter
#     def age(self, value):
#         self._age = value

# a = A()
# a.age = 18
# print(a.age)

# from functools import 

# 列表操作
a= [1,2,3]
print(a)
a.append(4)
print(a)
a.pop()
print(a)
a.pop(0)
print(a)


a[1:4]
print(a)
a[::-1]
print(a)


dp = [[0] *3 for _ in range(3)]
print(dp)

s="abxde"
print(s)
s[0]
s[1:4]
print(s)


# 字符串不可变
s = s[:0] + "x" + s[1:]

s.split()
print(s)

# dict
mp={}
# 获取字典中x的值，如果x不存在，则返回0
# 然后将其值加1
x=-0
mp[x]=mp.get(x,0)+1
print(mp)


from collections import defaultdict
# 默认值为0
mp = defaultdict(int)

# 默认值为1
mp = defaultdict(lambda: 1)
# 默认值为lambda: 1
print(mp)



st = set()
st.add(1)
3 in st

# 正向遍历
n=10
for i in range(n):
    pass
# 反向遍历
for i in range(n-1,-1,-1):
    pass


r=10
l=0
while l<=r:
    l+=1




def f(a,b):
    return a+b,a-b

x,y =f(5,3)

# 一维列表排序
arr=[1,2,3,4,5]
# 升序
arr.sort()
print(arr)
# 降序
arr.sort(reverse=True)
print(arr)

# 二维列表排序（按第二个元素）
arr = [[1, 3], [2, 1], [3, 4], [4, 2], [5, 5]]
# 按第二个元素升序
arr.sort(key=lambda x: x[1])
print(arr)
# 按第二个元素降序
arr.sort(key=lambda x: x[1], reverse=True)
print(arr)


import math
# 最大公约数
math.gcd(10,20)

# 最小公倍数
math.lcm(10,20)


from collections import deque

q = deque()
q.append(1)
q.append(2)
q.append(3)
q.append(4)
q.append(5)
print(q)
result=q.popleft()
print(result)
print(q)
# 最小堆
import heapq
heap=[]
heapq.heappush(heap,1)
heapq.heappush(heap,2)
heapq.heappush(heap,3)
heapq.heappush(heap,4)
heapq.heappush(heap,5)
print(heap)

result=heapq.heappop(heap)
print(result)
print(heap)

# 最大堆
# 使用负数实现最大堆
heapq.heappush(heap,-1)
heapq.heappush(heap,-2)
heapq.heappush(heap,-3)
heapq.heappush(heap,-4)
heapq.heappush(heap,-5)
print(heap)
result=heapq.heappop(heap)
print(result)
print(heap)


# 算法模版
# 1. 暴力枚举
for i in range(n):
    for j in range(n):
        pass
# 2. 双指针
l=0
r=n-1
while l<=r:
    l+=1
    r-=1


# 3. 二分查找
l=0
r=n-1
while l<=r:
    mid=(l+r)//2
    if arr[mid]==target:
        print(mid)
        break
    elif arr[mid]<target:
        l=mid+1
    else:
        r=mid-1

# 4. 贪心算法
for i in range(n):
    if arr[i]>arr[i+1]:
        print(arr[i])
        break

# 5. 动态规划
dp=[0]*(n+1)
dp[0]=1
dp[1]=1
for i in range(2,n+1):
    dp[i]=dp[i-1]+dp[i-2]
print(dp[n])
import pandas as pd
import numpy as np
# import torch

# Series
s1=pd.Series([1,'a',5,2,7])
print(s1)
print(s1.index)
print(s1.values)
s2=pd.Series([1,'a',5.2,7],index=['d','b','a','c'])
print(s2)
print(s2.index)
sdata={"asda":1,"asd":2}
s3=pd.Series(sdata)
print(s3)
print(s3["asda"])
print(type(s2["a"]))
print(s2[['b','a']])
print(type(s2[['c','a']]))
# DataFrame 表数据结构
# 每列可以是不同的数据类型
# 有每个行索引index 也有每个列索引columns
# 可以被看做Series 组成的字典

data={
    "state":s1,
    "year":s2,
    "pop":s3


}
df=pd.DataFrame(data)
data1={
    "state":[1,2,3],
    "year":[2,3,4],
    "pop":[3,4,5]

}
df2=pd.DataFrame(data1)
print(df2)


print(df)
print(df.columns)
print(df.index)

# 查询一列数据
print("查询year数据列的类型")
print(df["year"])
# 查看dataFrame中一列的数据类型
print(type(df["year"]))
# 查询多列数据额
print(df[["year","state"]])
# 查询多列数据类型
print(type(df[["year","state"]]))
# 查询一行数据
print(df.loc[1])
# 查询一行数据类型
print(type(df.loc[1]))
#查询多行数据
print(df.loc[1:3])
# 查询多行数据类型
print(type(df.loc[1:3]))

# pandas 数据类型查询

df2 = pd.read_excel("天气预报.xlsx")
print(df2)
# 当inplace 为True时直接修改
# inplace : bool, default False
#             Whether to modify the DataFrame rather than creating a new one.
df2.set_index("时间",inplace=True)
print(df2)
print(df2.index)

# 替换温度后缀
df2.loc[:,"最高温度"]= df2["最高温度"].str.replace("℃","").astype("int32")

print(df2.dtypes)
print(df2.head())
# 使用单个Lable值查询数据


df1=pd.DataFrame({'A':['A0','A1','A2','A3'],
                  'B':['B0','B2','B3','B4'],
                  'C':['C0','C1','C2','C3'],
                  'D':['D0','D1','D2','D3'],
                  })

print(df1)
df2=pd.DataFrame({
    'A':['A4','A5','A6','A7'],
    'B':['B4','B5','B6','B7'],
    'C':['c4','C5','C6','C7'],

})


print(pd.concat([df1,df2]))
print(pd.concat([df1,df2],ignore_index=True))
print(pd.concat([df1,df2],ignore_index=True,join="inner"))

s1=pd.Series(list(range(4)),name='F')
# 添加一列Series
print(pd.concat([df1,s1],axis=1))
# 添加多别Series
s2=df1.apply(lambda x:x['A']+"_GG",axis=1)
print(s2)
s2.name="G"
# 合并
print(pd.concat([df1,s1,s2],axis=1))
# 列表可以只是Series
print(pd.concat([s1,s2],axis=1))
# 列表可以是混合顺序
print(pd.concat([s1,df1,s2],axis=1))
# 使用DataFrame按照行合并数据
df1=pd.DataFrame([[1,2],[3,4]],columns=list('AB'))
print(df1)
df2=pd.DataFrame([[5,6],[7,8]],columns=list('AB'))
print(df2)
print(df._append(df2))
# 生成均匀分布的随机数
# 生成三行四列的张量
tensor=torch.rand((3,4))
print(tensor)
'''
tensor([[0.5944, 0.3480, 0.3809, 0.4361],
        [0.8518, 0.5741, 0.4286, 0.3816],
        [0.0749, 0.0744, 0.3144, 0.3763]])
'''
# 生成一个形状为（3,4）的张量 元素值服从标准正态分布
tensor=torch.randn((3,4))
print(tensor)
print("均值：" ,tensor.mean().item())
print("标准差",tensor.std().item())
'''
tensor([[-0.6911, -0.0696, -0.5529,  0.7557],
        [-1.2076,  0.6101, -1.3562,  0.0137],
        [-0.1792,  0.2590, -0.0362, -1.2091]])
均值： -0.3052833676338196
标准差 0.7053781747817993
'''
indices = torch.tensor([14])
print(indices)
'''
tensor([14])

'''
import pandas
import torch
import numpy

# 创建
array = numpy.array([[1,2,3],[4,5,6]])
print(array)
# 输出维度
print('number of dim',array.ndim)
# 输出行数列数
print('shape:',array.shape)
# 输出元素个数
print('size:',array.size)
# 创建矩阵 并制定类型
a=numpy.array([[2,3,4],[3,4,5]] ,dtype=int)

b=a.tolist()
print(b)



# 生成全零的矩阵
a=numpy.zeros([3,4])
print(a)
'''
[[0. 0. 0. 0.]
 [0. 0. 0. 0.]
 [0. 0. 0. 0.]]
'''
# 生成全部为一的矩阵
b=numpy.ones((3,4))
print(b)
'''
[[1. 1. 1. 1.]
 [1. 1. 1. 1.]
 [1. 1. 1. 1.]]
'''
a=numpy.arange(10,20,3)
print(a)
'''
[10 13 16 19]
'''
a=numpy.linspace(1,10,6).reshape((2,3))
print(a)
'''
[[ 1.   2.8  4.6]
 [ 6.4  8.2 10. ]]
'''

# numpy的索引
A=numpy.arange(3,15).reshape((3,4))
print(A)
'''
[[ 3  4  5  6]
 [ 7  8  9 10]
 [11 12 13 14]]
'''
# 输出第三行
print(A[2])
'''
[11 12 13 14]
'''

print(A[1][1])
print(A[1,1])
'''
8
8
'''
print(A[2,:])
'''
[11 12 13 14]
'''

# 输出某一列
print(A[:,1])
'''
[ 4  8 12]

'''
# 迭代每一行
for row in A:
    print(row)
'''
[3 4 5 6]
[ 7  8  9 10]
[11 12 13 14]
'''

#转置
print(A.T)
'''
[[ 3  7 11]
 [ 4  8 12]
 [ 5  9 13]
 [ 6 10 14]]
'''

# 迭代每一列
for column in A.T:
    print(column)
'''
[ 3  7 11]
[ 4  8 12]
[ 5  9 13]
[ 6 10 14]
'''
# 将矩阵展平
print(A.flatten())
'''[ 3  4  5  6  7  8  9 10 11 12 13 14]'''


# 遍历每个值
for item in A.flat:
    print(item)
'''
3
4
5
6
7
8
9
10
11
12
13
14
'''

# numpy array 合并
A = numpy.array([1,1,1])
B=numpy.array([2,2,2])
# 上下合并 vertical stack
C=numpy.vstack((A,B))
print(C)
'''
[[1 1 1]
 [2 2 2]]
'''
print(A.shape,C.shape)
'''
(3,) (2, 3)

'''
# 左右合并 horizontal stack
D=numpy.hstack((A,B))
print(D)
'''
[1 1 1 2 2 2]
'''
print(A.shape,D.shape)
'''
(3,) (6,)
'''
# 横行数列改为竖行数列
print(A[:,numpy.newaxis])
'''
[[1]
 [1]
 [1]]
'''

A=numpy.array([1,1,1])[:,numpy.newaxis]
B=numpy.array([2,2,2])[:,numpy.newaxis]
# axis=0 时上下方向合并
C=numpy.concatenate((A,B,A,B),axis=0)
print(C)
'''
[[1]
 [1]
 [1]]
[[1]
 [1]
 [1]
 [2]
 [2]
 [2]
 [1]
 [1]
 [1]
 [2]
 [2]
 [2]]
'''
#  axis=1 时水平方向合并
C=numpy.concatenate((A,B,A,B),axis=1)
print(C)
'''
[[1 2 1 2]
 [1 2 1 2]
 [1 2 1 2]]
'''
# numpy 分割
A=numpy.arange(12).reshape((3,4))
print(A)
'''
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
'''

# 只能进行相等的分割
print(numpy.split(A,2,axis=1))
'''
[array([[0, 1],
       [4, 5],
       [8, 9]]), array([[ 2,  3],
       [ 6,  7],
       [10, 11]])]
'''
# 进行不等量的分割
print(numpy.array_split(A,3,axis=1))

'''
[array([[0, 1],
       [4, 5],
       [8, 9]]), array([[ 2,  3],
       [ 6,  7],
       [10, 11]])]
'''

# 水平分割
print(numpy.vsplit(A,3))
'''
[array([[0, 1, 2, 3]]), array([[4, 5, 6, 7]]), array([[ 8,  9, 10, 11]])]
'''
# 垂直分割
print(numpy.hsplit(A,2))
'''
[array([[0, 1],
       [4, 5],
       [8, 9]]), array([[ 2,  3],
       [ 6,  7],
       [10, 11]])]

'''
# numpy array copy
a=numpy.arange(4)
print(a)
'''
[0 1 2 3]
'''
a[0]=1
b=a
c=a
d=b
print(a)
'''
[1 1 2 3]
'''
b[2]=1
print(b)
'''
[1 1 1 3]
'''
print(a)
'''
[1 1 1 3]
'''

print(b is a)
'''
True
'''

print(c)
'''
[1 1 1 3]
'''

print(d is a)
'''
True
'''
d[1:3]=[22,33]
print(a)
'''
[ 1 22 33  3]
'''
# 复制时 不想关联
b=a.copy()
a[3]=44
print(a)
'''
[ 1 22 33 44]
'''
print(b)
'''
[ 1 22 33  3]
'''


s =pandas.Series([1,2,4,numpy.nan,44,1])
print(s)
'''
0     1.0
1     2.0
2     4.0
3     NaN
4    44.0
5     1.0
dtype: float64
'''
datas= pandas.date_range('20160101',periods=6)
print(datas)
'''
DatetimeIndex(['2016-01-01', '2016-01-02', '2016-01-03', '2016-01-04',
               '2016-01-05', '2016-01-06'],
              dtype='datetime64[ns]', freq='D')
'''
# index 代表行 columns 代表列
df=pandas.DataFrame(numpy.random.randn(6,4),index=datas,columns=['a','b','c','d'])
print(df)
'''
                   a         b         c         d
2016-01-01  0.602516  1.608001  2.171642 -0.587538
2016-01-02  1.239168  0.497224  0.728967 -1.440362
2016-01-03 -0.876627  0.944289  0.013055 -1.309509
2016-01-04  0.645842 -0.683205  0.241934 -0.817849
2016-01-05  1.559710  0.726065  0.115998  0.802615
2016-01-06  0.161373 -1.398195 -0.112761 -0.228360

'''

df1=pandas.DataFrame(numpy.arange(12).reshape(3,4))
print(df1)
'''
   0  1   2   3
0  0  1   2   3
1  4  5   6   7
2  8  9  10  11
'''
# 创建张量
x = torch.arange(12)
print(x)
'''
tensor([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11])
'''
# 改变张量的元素而不改变张量的数量和元素值
# 改成三行四列
x=x.reshape(3,4)
print(x)
'''
tensor([[ 0,  1,  2,  3],
        [ 4,  5,  6,  7],
        [ 8,  9, 10, 11]])

'''
# 创建特殊常量
print(torch.zeros((2,3,4)))
'''
tensor([[[0., 0., 0., 0.],
         [0., 0., 0., 0.],
         [0., 0., 0., 0.]],

        [[0., 0., 0., 0.],
         [0., 0., 0., 0.],
         [0., 0., 0., 0.]]])
'''
print(torch.ones((2,4)))
'''
tensor([[1., 1., 1., 1.],
        [1., 1., 1., 1.]])
'''
#通过python列表(或者嵌套列表）来为每个张量中每个元素赋值
print(torch.tensor([[1,2,3],[4,5,6]]))
'''
tensor([[1, 2, 3],
        [4, 5, 6]])
'''
# 进行常见的算数运算 （+ - * 、 **）
x=torch.tensor([1,0,2,4,8])
y=torch.tensor([2,2,3,2,5])
print(x+y,x-y,x*y,x/y,x**y)
'''
tensor([ 3,  2,  5,  6, 13]) tensor([-1, -2, -1, 2,  3]) tensor([ 2,  0,  6,  8, 40]) tensor([0.5000, 0.0000, 0.6667, 2.0000, 1.6000]) tensor([    1,     0,     8,    16, 32768])
'''
# 按照元素方式计算更多运算 指数运算
print(torch.exp(x))
'''
tensor([2.7183e+00, 1.0000e+00, 7.3891e+00, 5.4598e+01, 2.9810e+03])
'''
# 我们可以把张量连接在一起
x=torch.arange(12,dtype=torch.float32).reshape((3,4))
y=torch.tensor([[2.0,1,4,3],[1,2,3,4],[4,3,2,1]])
# 行连接
print(torch.cat((x,y),dim=0))
'''
tensor([[ 0.,  1.,  2.,  3.],
        [ 4.,  5.,  6.,  7.],
        [ 8.,  9., 10., 11.],
        [ 2.,  1.,  4.,  3.],
        [ 1.,  2.,  3.,  4.],
        [ 4.,  3.,  2.,  1.]])
'''

print(torch.cat((x,y),dim=1))
'''
tensor([[ 0.,  1.,  2.,  3.,  2.,  1.,  4.,  3.],
        [ 4.,  5.,  6.,  7.,  1.,  2.,  3.,  4.],
        [ 8.,  9., 10., 11.,  4.,  3.,  2.,  1.]])
'''
# 逻辑运算符构建二元变量
print(x==y)
'''
tensor([[False,  True, False,  True],
        [False, False, False, False],
        [False, False, False, False]])
'''
# 张量中进行所有元素求和
print(x.sum())
'''
tensor(66.)
'''
# 即使形状不一样 我们仍然可以调用广播机制

a=torch.arange(3).reshape((3,1))
b=torch.arange((2)).reshape((1,2))
print(a+b)
'''
tensor([[0, 1],
        [1, 2],
        [2, 3]])
'''
# 元素的访问
print(x[-1])
'''
tensor([ 8.,  9., 10., 11.])
'''
# 第一行和第二行
print(x[1:3])
"""
tensor([[ 4.,  5.,  6.,  7.],
        [ 8.,  9., 10., 11.]])
"""
#通过索引设置元素的值
x[2,2]=0
print(x)
'''
tensor([[ 0.,  1.,  2.,  3.],
        [ 4.,  5.,  6.,  7.],
        [ 8.,  9.,  0., 11.]])

'''
# 为多个元素赋值相同的元素
# 第一行到第三行的所有列
x[0:2,:]=12
print(x)
'''
tensor([[12., 12., 12., 12.],
        [12., 12., 12., 12.],
        [ 8.,  9.,  0., 11.]])

'''
# 运次操作可能出现导致出现新的结果分配内存
before = id(y)
y=y+x
print(id(y) == before)
"""
False
"""
# 执行原地操作
z=torch.zeros_like(y)
print("id(z):",id(z))
z[:]=x+y
print("id(z)",id(z))
"""
id(z): 2229072232816
id(z) 2229072232816
"""
# r=如果后续计算没有重复使用x
before = id(x)
x+=y
print(id(x) == before)
'''
True
'''
# 转换为Numpy张量
A = x.numpy()
B = torch.tensor(A)
print(type(A),type(B))
'''
<class 'numpy.ndarray'> <class 'torch.Tensor'>
'''
# 将一个大小为1的张量转换为python标量
a = torch.tensor([3.5])
print(a,a.item(),float(a),int(a))
'''
tensor([3.5000]) 3.5 3.5 3
'''
# 快速定义均匀间隔的数值序列
# 指定间隔初始点、终止端、以及指定分隔值总数
print(numpy.linspace(start = 0, stop = 100, num = 5))
'''
[  0.  25.  50.  75. 100.]
'''
# ndpoint 参数决定终止值是否被包含在结果数组中。缺省为True，即包括在结果中，反之不包括
print(numpy.linspace(start= 1, stop=5,num=4,endpoint=False))
'''
[1. 2. 3. 4.]
'''
print(type(numpy.linspace(1,88,9)))
'''
[1. 2. 3. 4.]
'''

print(numpy.linspace(1,10,4).reshape(4,1))
'''
[[ 1.]
 [ 4.]
 [ 7.]
 [10.]]
'''
# 使用zeros_like创建数值为0形状相同的张量
x1  = numpy.linspace(1,10,5).reshape(5,1)
print((numpy.zeros_like(x1)+2)+numpy.random.rand(5,1)*0.1)
'''
[[2.01847187]
 [2.04983068]
 [2.04948751]
 [2.09579782]
 [2.09052877]]
'''
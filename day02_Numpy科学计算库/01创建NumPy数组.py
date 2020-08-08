# 安装NumPy库
# pip install numpy
# 导入NumPy库
# import numpy as np 在调用Numpy中的函数时，一定要加上前缀np
# from numpy import * 在调用Numpy中的函数时，可以不加前缀
import numpy as np

# 创建数组 输出指定的数组元素
# array([列表]/(元组))
a = np.array([0, 1, 2, 3])
b = np.array((1, 2, 3, 4))
print(a, " "*3, b)
for i in a:
    print(b[i], end=" ")
print(a[0:])
print(a[:3])
print(a[1:3])

# 数组的属性
# ndim 数组的维数
print("数组的维数:", a.ndim)
# shape 数组的形状
print("数组的形状:", a.shape)
# size 数组元素的总个数
print("数组元素的总个数:", a.size)
# dtype 数组中元素的数据类型
print("数组中元素的数据类型:", a.dtype)
# itemsize 数组中每个元素的字节数
print("数组中每个元素的字节数:", a.itemsize)

# 二维数组
b = np.array([[0, 1, 2, 3],
              [4, 5, 6, 7],
              [8, 9, 10, 11]])
print(b)
print(b.ndim, b.shape, b.size, b.dtype, b.itemsize)
for i in b:
    for j in i:
        print(j, end=" ")
print(b[2][3])

# 三维数组
c = np.array([[[0, 1, 2, 3],
               [4, 5, 6, 7],
               [8, 9, 10, 11]],
              [[12, 13, 14, 15],
               [16, 17, 18, 19],
               [20, 21, 22, 23]]])
print(c)
print(c.ndim, c.shape,c.size, c.itemsize, c.dtype)
for i in c:
    for j in i:
        for k in j:
            print(k, end=" ")
print()
print(c[0])
print(c[0][0])

# 数组元素的数据类型 NumPy要求数组中所有元素的数据类型必须是一致的
# array([列表]/(元组), dtype=数据类型)
A = np.array([0, 1.1, 2, 3], dtype=np.int64)
print(A)
B = np.array([0, 1.1, 2, 3])
print(B, B.dtype)

# 创建特殊的数组
# arange()函数:创建一个由数字序列构成的数组。
# np.arange( 起始数字, 结束数字, 步长, dtype )
# 前闭后开:数字序列中不包括结束数字
# 起始数字省略时，默认从0开始
# 步长省略时，默认为1
d = np.arange(4)
print(d)
d = np.arange(1, 3, 0.5,)
print(d)

#  ones()函数:创建一个元素全部为1的数组
# np.ones( shape, dtype ) dtype默认float64
e = np.ones((3, 3), np.int64)
print(e)
print(e.dtype)

# zeros()函数:创建一个元素全部为0的数组
# np.zeros( shape, dtype )
f = np.zeros((2, 2), np.int64)
print(f)
print(f.dtype)

# eye()函数:创建一个单位矩阵
# np.eye( shape, dtype )
h = np.eye(2, 3)
print(h, h.dtype)
h = np.eye(3)
print(h, h.shape)

# linspace()函数:创建等差数列
# np.linspace(start, stop, num=50, dtype) 参数:起始数字、结束数字、元素个数、元素数据类型
g = np.linspace(1, 10, 5)
print(g, g.dtype, g.shape)

# logspace()函数:创建一个等比数列
# np.logspace(start, stop, num=50, base=10, dtype) 参数:起始指数、结束指数、元素个数、基、、元素数据类型
j = np.logspace(2, 4, num=3, base=2,)
print(j)

# asarray()函数:将列表或元组转化为数组对象
lst_1 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
arr_1 = np.array(lst_1)
arr_2 = np.asarray(lst_1)
lst_1[0][0] = 3
print("list1:\n", lst_1)
print("arr1:\n", arr_1)
print("arr2:\n", arr_2)
# 区别：
# 当数据源本身是一个ndarray对象时，array()会复制出一个副本，占用新 的内存，而asarray()则不复制副本, 它直接引用原数组。
arr_3 = np.ones((3, 3))
arr_4 = np.array(arr_3)
arr_5 = np.asarray(arr_3)
arr_3[0][0] = 3
print("arr_3:\n", arr_3)
print("arr_4:\n", arr_4)
print("arr_5:\n", arr_5)
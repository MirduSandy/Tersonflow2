# 1.数组元素的切片
# 可以使用切片来访问NumPy数组中的一部分，切片方法和Python序列 数据结构的切片一样
# 一维数组
import numpy as np
a = np.array([1, 2, 3, 4])
print(a[:], a[1:3])

# 二维数组
b = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])
print(b[:])
print(b[0:2])
print(b[:, 0:2])
print(b[:, 0])

# 三维数组
c = np.array([[[1, 2, 3, 4],
               [5, 6, 7, 8]],
              [[9, 10, 11, 12],
              [13, 14, 15, 16]]])
print(c.ndim)
print(c[:])
print(c[:, 0:1, 0])
print(c[:, :, 1])

# 2.改变数组的形状
# np.reshape(shape) 不改变当前数组，按照shape创建新的数组 return array
d = np.arange(0, 12, 1)
print(d)
print(d.reshape(3, 4))
print(d)

# np.resize(shape) 改变当前数组，按照shape创建数组 return None
e = np.arange(0, 12, 1)
print(e)
print(e.resize(3, 4))
print(e)

# 当改变形状时，应该考虑到数组中元素的个数，确保改变前后，元素总个数相
# 创建数组并且改变数组形状
d = np.arange(0, 12, 1).reshape(3, 4)
print(d)

# 参数-1:根据数组中元素总个数、以及 其他维度的取值，来自动计算出这个维 度的取值。
b = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])
print(b.reshape(-1, 3)) #(4, 3)
print(b.reshape(-1, 4)) #(3, 4)
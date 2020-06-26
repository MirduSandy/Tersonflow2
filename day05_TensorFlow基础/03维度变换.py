import tensorflow as tf
import numpy as np
# 改变张量的形状
# tf.reshape(tensor, shape)
a = tf.range(1, 12, delta=2)
print(a)
print(tf.reshape(a, (2, 3)))

b = tf.constant(np.arange(24).reshape(2, 3, 4))
print(b)
# shape参数=-1: 自动推导出长度
print(tf.reshape(b, (4, -1)))

# 增加和删除维度
# 增加维度
# tf.expand_dims(输入张量input, 要增加维度数axis)  在axis=1的轴上增加维度
t = tf.constant([1, 2])
print("t:", t, t.shape)
t1 = tf.expand_dims(t, 1)
print("t1:", t1, t1.shape)
t2 = tf.expand_dims(t1, 1)
print("t2:", t2, t2.shape)
# t3 = tf.expand_dims(t, 2)
# print(t3, t3.shape)
# 当axis=0时,在0维上加1
t5 = tf.expand_dims(t, 0)
print("t5:", t5, t5.shape)
t6 = tf.expand_dims(t, -1)
print("t6:", t6, t6.shape)

print("b:", b, b.shape)
b1 = tf.expand_dims(b, 0)
b2 = tf.expand_dims(b, 1)
b3 = tf.expand_dims(b, 2)
b4 = tf.expand_dims(b, 3)
print("b1:", b1, b1.shape)
print("b2:", b2.shape)
print("b3:", b3.shape)
print("b4:", b4.shape)


# 删除维度
# tf.squeeze(原始张量input, 要删除的维度axis=None）
# 只能删除长度为 1 的维度， 省略时删除所有长度为1的维度
b5 = tf.expand_dims(b1, 4)
print("b5:", b5.shape)
b6 = tf.squeeze(b5)
print("b6:", b6, tf.shape(b6))
b7 = tf.squeeze(b5, 4)
print(tf.shape(b7))

# 交换维度 tf.transpose(输入张量a, 调整张量中的各个轴的顺序perm)
c = tf.constant([[1, 2, 3], [4, 5, 6]])
print(c)
print(tf.transpose(c))
print(tf.transpose(c, perm=(1, 0)))

d = tf.reshape(tf.range(24), (2, 3, 4))
print("d", d)
print("d1", tf.transpose(d, (1, 0, 2)))

# 拼接和分割
# tf.concat(所有需要拼接的张量列表tensors, 指定在哪个轴上进行拼接axis)
# 拼接张量
# 将多个张量在某个维度上合并
# 拼接并不会产生 新的维度
f1 = [[1, 2, 3], [4, 5, 6]]
f2 = [[7, 8, 9], [10, 11, 12]]
print(type(f1), ";", type(f2))
print(tf.concat([f1, f2], 0)) #在axis=0的轴上拼接
print(tf.concat([f1, f2], 1)) #在axis=1的轴上拼接

# 分割张量:将一个张量拆分成多个张量，分割后维度不变
# tf.split(待分割张量value,分割方案num_or_size_splits, 指明分割的轴axis=0 )
# 分割方案:
# 是一个数值时，表示等长分割，数值是切割的份数;
# 是一个列表时，表示不等长切割，列表中是切割后每份的长度
# 2 :分割成2个张量
# [1:2:1]:就表示分割成3个张量，长度分别是1,2,1

g = tf.reshape(tf.range(24), (4, 6))
print(g)
print(tf.split(g, 2, 0))
print(tf.split(g, [2, 1, 1], 0))
# 图像的分割与拼接，改变了张量的视图，张量的存储顺序并没有改变。


# 堆叠和分解
# 堆叠张量
# n 在合并张量时， 创建一个新的维度
# n 和NumPy中堆叠函 数的功能完全一样
# tf.stack(要堆叠的多个张量values, 指定插入新维度的位置axis)
h1 = tf.constant([1, 2, 3])
h2 = tf.constant([4, 5, 6])
print(tf.stack((h1, h2), axis=0))
print(tf.stack((h1, h2), axis=1))

# 分解张量
# tf.unstack(values, axis)
# n 是张量堆叠的逆运算
# n 张量分解为多个张量
# n 分解后得到的每个张量，和原来的张量相比，维数都少了一维
j = tf.constant([[1, 2, 3], [4, 5, 6]])
print(tf.unstack(j, axis=0))

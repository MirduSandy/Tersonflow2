# 索引和切片
# 索引 a[1][1][1]  === a[1,1,1]
# 切片 a[起始位置:结束位置: 步长]
# n 起始位置:结束位置，是前闭后开的，切片中不包含结束位置
# n 起始位置、结束位置、步长都可以省略
# n 步长可以是负数，这时起始位置的索引号，应该大于结束位置
import tensorflow as tf
# 一维张量切片
a = tf.range(10)
print(a[1])
print(a[::])
print(a[1:10:2])
print(a[::2])
print(a[10:0:-1])
print(a[::-1])

# 下载鸢尾花数据集
Train_Url = "http://download.tensorflow.org/data/iris_training.csv"
Train_Path = tf.keras.utils.get_file(Train_Url.split("/")[-1], Train_Url)
import pandas as pd
# 使用pandas读取到二维表格对象df_iris中
df_iris = pd.read_csv(Train_Path)
import numpy as np
# 转换为NumPy数组np_iris
np_iris = np.array(df_iris)
iris = tf.convert_to_tensor(np_iris)
print(iris.shape)

# 二维张量切片:维度之间用逗号隔开
# 读取第一个样本的所有lie
print(iris[0, :])
# 读取前5个样本的所有的属性
print(iris[0:5, 0:4])

# 采用切片的方式，只能进行连续的、或者有规律的采样
mnist = tf.keras.datasets.mnist
# print(type(mnist))
(train_x, train_y), (test_x, test_y) = mnist.load_data()
# print(type(train_x))
print(train_x.shape)
print(train_x[0, :, :])

# 数据提取:根据索引，抽取出没有规律的、特定的数据
# gather(输入张量param,  索引值列表indices)函数:用一个索引列表，将给定张量中对应索引值的
# 元素提取出来
a = tf.range(20)
print(a, type(a))
print(tf.gather(a, indices=(0, 2, 3)))

# 对多维张量采样——gather()、gather_nd()函数
# gather( params, 轴axis, indices )
b = tf.reshape(a, (4, 5))
print(b)
print(tf.gather(b, axis=1, indices=(0, 1)))
print(tf.gather(b, axis=0, indices=(0, 1)))

# 同时采样多个点——gather_nd()函数
# n 通过指定坐标,同时采样多个点
# n 可以同时对多个维度进行索引
print(tf.gather_nd(b, indices=[[0, 0], [1, 1], [2, 2]]))

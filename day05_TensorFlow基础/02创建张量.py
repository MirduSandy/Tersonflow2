import tensorflow as tf
# 查看版本号
print("Tensorflow version:", tf.__version__)
# 2.0的版本号默认为为EagerExecution模式
print("Eager execution is:", tf.executing_eagerly())

# n Python列表(list):[]
# p 元素可以使用不同的数据类型，可以嵌套
# p 在内存中不是连续存放的，是一个动态的指针数组
# p 读写效率低，占用内存空间大
# p 不适合做数值计算

# NumPy数组(ndarray):
# p 元素数据类型相同
# p 每个元素在内存中占用的空间相同，存储在一个连续的内存区域中
# p 存储空间小，读取和写入速度快
# p 不能够主动检测利用GPU进行运算

# TensorFlow张量(Tensor):
# p 可以高速运行于GPU和TPU之上，实现神经网络和深度学习中的复杂算法


#  方法一：创建Tensor对象
# 张量由Tensor类实现，每个张量都是一个Tensor对象
# p tf.constant()函数:创建张量
#            tf.constant(value, dtype, shape)
# n value:数字/Python列表/NumPy数组
# n dtype: 元素的数据类型
# n shape: 张量的形状

# 参数为Python列表
a = tf.constant([[1, 2], [3, 4]])
print("a:", a)

# 张量的.numpy()方法  张量转化为数组
b = a.numpy()
print("b:", b)

print("a_type:", type(a))
print("b_type:", type(b))

# 参数为数字
c = tf.constant(1.0)
print("c:", c)
print(tf.constant(1.))
print(tf.constant(1))      # shape=() 0维张量
# 指定元素的数据类型
d = tf.constant(1.0, dtype=tf.float64)
print(d)

# 参数为Numpy数组
import numpy as np
e = tf.constant(np.array([1, 2]))
print(e)
f = tf.constant(np.array([1.0, 2.0]))
print(f)

#  tf.cast()函数:改变张量中元素的数据类型  tf.cast(x,dtype)
g = tf.cast(f, dtype=tf.int32)
print(g.dtype)

# 在进行数据类型转换时，一般是将低精度的数据类型向高精度转换，
# 否则可能发生数据溢出，得到错误的结果。
h = tf.constant(1234567890, dtype=tf.int32)
print(tf.cast(h, tf.int16))

# 参数为布尔型
print(tf.constant(True))
print(tf.cast(tf.constant([True, False]), tf.int32))
print(tf.cast(tf.constant([1, 0, 2, 3, -2]), tf.bool))  # 整型变量转换为布尔型，将非 0 数字都视为 True

# 参数为字符串
print(tf.constant("hello Tensor"))
# b:表示这是一个字节串。
# 在Python3中，字符串默认是Unicode编码， 因此要转成字节串，就在原来的字符串前面加上一个b

# 方法二：tf.convert_to_tensor()函数
# tf.convert_to_tensor( 数组/列表/数字/布尔型/字符串)
na = np.arange(12).reshape(3, 4)
print(na)
ta = tf.convert_to_tensor(na)
print(ta)

print("na_type:", type(na))
print("ta_type:", type(ta))

# is_tensor()函数 判断是不是张量
print(tf.is_tensor(ta))
print(tf.is_tensor(na))

# isinstance()函数
print(isinstance(ta, tf.Tensor))
print(isinstance(na, np.ndarray))

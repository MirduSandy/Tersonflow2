# 基本数学运算
# 加减乘除运算
import tensorflow as tf
a = tf.constant([1, 2, 3])
b = tf.convert_to_tensor([4, 5, 6])
print(tf.add(a, b))

# tf.add(x, y)将x和y逐元素相加
# tf.subtract(x, y)将x和y逐元素相减
# tf.multiply(x, y)将x和y逐元素相乘
# tf.divide(x, y)将x和y逐元素相除
# tf.math.mod(x, y)对x逐元素取模


# 算术操作
# tf.pow(x, y)
# tf.square(x)
# tf.sqrt(x)
# tf.exp(x)
# tf.math.log(x)
# 描述
# 对x求y的幂次方
# 对x逐元素求计算平方
# 对x逐元素开平方根
# 计算e的x次方
# 计算自然对数, 底数为e

# 一维张量幂运算
x = tf.range(4)
print(x)
print(tf.pow(x, 3))
print(tf.square(x))

# 二维张量幂运算
y = tf.constant([[2, 2], [3, 3]])
z = tf.constant([[8, 16], [2, 3]])
print(tf.pow(y, z))

c = tf.constant([1., 4., 9., 16.])
print(tf.pow(c, 0.5))

# 平方和平方根运算
d = tf.constant([1, 2, 3, 4])
print(tf.square(d))
print(tf.sqrt(c))
e = tf.constant([[1., 9.], [16., 100.]])
print(tf.sqrt(e))

# 自然指数和自然对数运算
# TensorFlow中只有以e为底的自然对数，没有提供以其他数值为底的对数运算函数
print(tf.exp(1.))
f = tf.exp(3.)
print(tf.math.log(f))

# 对数运算
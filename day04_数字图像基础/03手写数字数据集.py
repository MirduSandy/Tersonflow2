# 手写数字数据集
# MNIST数据集 Mixed National Institute of standards and Technology database
#  New York University，Yann LeCun
#  60000条训练数据和10000条测试数据
#  由250个不同的人手写而成
#  28×28像素, 灰度图像
#  存储在28×28的二维数组中

# 下载MNIST数据集
import tensorflow as tf
# 必须导入ssl请求证书
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
# 导入plt
import matplotlib.pyplot as plt
# 导入numpy
import numpy as np

mnist = tf.keras.datasets.mnist
(train_x, train_y), (test_x, test_y) = mnist.load_data()

# 测试集和训练集的长度
print("Training set:", len(train_x))
print("Testing set:", len(test_x))

# 查看训练集的数据纬度和类型
print("train_x:", train_x.shape, train_x.dtype)
print("train_y:", train_y.shape, train_x.dtype)

# 显示训练集数据
print("train_x内容：", train_x)
print("train_y内容：", train_y)

# 显示手写图片
# 1.绘图plt大小
plt.figure(figsize=(8, 8))
# 2.查看train_x类型
print(type(train_x))  # <class 'numpy.ndarray'>
# 3.显示图片 plt.imshow(图片对象/numpy数组对象)
plt.imshow(train_x[0], cmap="gray")    # 对应着train_y[0] = 5
# 4.显示plt
# plt.show()

# 随机显示4幅图片
# 1.for循环range(4)
for i in range(4):
    # 2.随机产生4个数 np.random.randint==>引入numpy
    num = np.random.randint(1, 50000)
    # 3.绘制4个子图
    plt.subplot(1, 4, i+1)
    plt.imshow(train_x[num], cmap="gray")
    # 4.加标题，设置中文
    plt.rcParams["font.sans-serif"] = "Arial Unicode MS"
    plt.title("这是第"+str(i+1)+"幅图片："+str(train_y[num]))

plt.show()


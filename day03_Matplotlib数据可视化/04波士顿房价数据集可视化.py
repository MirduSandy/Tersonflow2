import tensorflow as tf
#这是由于大部分https的网站需要有SSL证书，即使模拟了User-Agent访问，还是报错，https的安全基础是SSL，如果没有SSL证书，就会拒绝访问。
# 或者就是此次访问忽略证书验证:具体见https://blog.csdn.net/weixin_44129464/article/details/88079617?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase
# import ssl
import matplotlib.pyplot as plt
import numpy as np
# ssl._create_default_https_context = ssl._create_unverified_context
# Keras
# 是一个高层的神经网络和深度学习库。
# 可以快速搭建神经网络模型，非常易于调试和扩展。
# TensorFlow的官方API
# 内置了一些常用的公共数据集，可以通过keras.datasets模块加载和访问。

# 加载数据集——.load_data()方法
boston_housing = tf.keras.datasets.boston_housing
# 训练数据集          测试数据集
(train_x, train_y), (test_x, test_y) = boston_housing.load_data()

# 训练集合测试集
print("Training set:", len(train_x))
print("Testing set:", len(test_x))

# 改变数据集划分比例
(train_x, train_y), (test_x, test_y) = boston_housing.load_data(test_split=0)  #提取出全部数据作为训练集

print("Training set:", len(train_x))
print("Testing set:", len(test_x))

print(type(train_x))
print(type(train_y))

print("Dim of train_x:", train_x.ndim)
print("shape of train_x:", train_x.shape)

print("Dim of train_y:", train_y.ndim)
print("shape of train_y:", train_y.shape)

# 访问数据集中的数据——输出train_x中的前5行数据
print(train_x[0:5])

# 访问数据集中的数据——输出train_x中的第6列数据
print(train_x[:, 5])

# 访问数据集中的数据——输出train_y中的全部数据
print("train_y:", train_y)
print("train_x:", train_x)

# 将平均房间数与房价之间的关系可视化
# 设置绘图尺寸
plt.figure(figsize=(5, 5))
# 绘制散点图
plt.scatter(train_x[:, 5], train_y)
# x轴名称
plt.xlabel("RM")
# y轴名称
plt.ylabel("price($1000's)")
# 设置标题
plt.title("5. RM-Price")
# 显示绘图
plt.show()

# 将所有属性与房价之间的关系可视化
# 设置字体显示中文
plt.rcParams["font.sans-serif"] = "Arial Unicode MS"
# 设置标题list
titles = ["CRIM", "ZN", "INDUS", "NOX", "RM", "AGE", "DIS", "RAD", "TAX", "PTRATIO", "B-1000", "LSTAT", "MEDV"]
# 设置绘图尺寸
plt.figure(figsize=(12, 12))
# for循环显示关系
for i in range(13):
    # 设置子图尺寸和排序
    plt.subplot(4, 4, (i+1))
    # 绘制散点图
    plt.scatter(train_x[:, i], train_y)
    # 设置x轴y轴文本标签
    plt.xlabel(titles[i])
    plt.ylabel("price($1000's)")
    # 设置子图标题
    plt.title(str(i+1)+"."+titles[i]+"- Price")

# 自动调整子图布局
plt.tight_layout()
# 设置全局标题
plt.suptitle("各属性与房价之间的关系", x=0.5, y=1.02, fontsize=20)
# 显示散点图
plt.show()


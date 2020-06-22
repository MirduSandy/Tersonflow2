import tensorflow as tf
import numpy as np
# pandas 是基于NumPy 的一种工具，该工具是为了解决数据分析任务而创建的。
import pandas as pd
import matplotlib.pyplot as plt
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# get_file函数 下载数据集
# tf.keras.utils.get_file(fname, origin, cache_dir)
# 参数
# fname: 下载后的文件名;
# origin: 文件的URL地址;
# cache_dir: 下载后文件的存储位置。C:\Users\\Administrator\.keras\datasets
# 返回值: 下载后的文件在本地磁盘中的绝对路径。
Train_Url = "http://download.tensorflow.org/data/iris_training.csv"
# Train_Path = tf.keras.utils.get_file("iris_trainning.csv", Train_Url)
# split 函数返回list
print(Train_Url.split('/'))
# 获取文件名
print(Train_Url.split("/")[-1])
Train_Path = tf.keras.utils.get_file(Train_Url.split("/")[-1], Train_Url)

# 打印鸢尾花数据集
COLLUMN_NAMES = ['SepallLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'Species']
df_iris = pd.read_csv(Train_Path, names=COLLUMN_NAMES, header=0)
iris = np.array(df_iris)
print(iris, iris.shape)
print(iris[:, 2])
# 可视化
# 绘制散点图
plt.scatter(iris[:, 2], iris[:, 3], c=iris[:, 4], cmap='brg')
plt.title("Anderson's Iris Data Set \n(Bule_>Setosa | Red_>Versicolor | Green_>Virginica)")
plt.xlabel(COLLUMN_NAMES[2])
plt.ylabel(COLLUMN_NAMES[3])
plt.show()


# 所有属性可视化
fig = plt.figure('Iris Data', figsize=(15, 15))
fig.suptitle("Anderson's Iris Data Set \n(Bule_>Setosa | Red_>Versicolor | Green_>Virginica)", fontsize=20)

for i in range(4):
    for j in range(4):
        plt.subplot(4, 4, 4*i + (j + 1))
        if(i == j):
            plt.text(0.3, 0.4, COLLUMN_NAMES[i], fontsize=15)
        else:
            plt.scatter(iris[:, j], iris[:, i], c=iris[:, 4], cmap='brg')
        if(i == 0):
            plt.title(COLLUMN_NAMES[j])
        if(j == 0):
            plt.ylabel(COLLUMN_NAMES[i])
plt.show()


# 散点图(Scatter):是数据点在直角坐标系中的分布图
# scatter() 函数 scatter( x, y, scale, color, marker, label )
# 绘制标准正态分布的散点图
# 导入绘图库
import matplotlib.pyplot as plt
# 导入numpy库
import numpy as np

# 设置字体
plt.rcParams["font.sans-serif"] = "Arial Unicode MS"

n = 1024                         # 随机点的个数：1024
x = np.random.normal(0, 1, n)    # 生成数据点x坐标
y = np.random.normal(0, 1, n)    # 生成数据点y坐标

# 绘制散点图
plt.scatter(x, y, color="blue", marker="o")


plt.title("标准正态分布", fontsize=20)    # 设置标题
plt.text(2.5, 2.5, "均   值 ：0\n标准差：1")  # 设置文本

# 设置坐标轴范围
plt.xlim(-4, 4)   # x轴范围
plt.ylim(-4, 4)   # y轴范围

plt.xlabel("横坐标x", fontsize=14)    # 设置x轴标签文本
plt.ylabel("纵坐标y", fontsize=14)    # 设置y轴标签文本
plt.show()  # 显示绘图

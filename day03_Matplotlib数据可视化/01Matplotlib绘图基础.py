# 安装Matplotlib库 pip install matplotlib
#  导入Matplotlib库
import matplotlib.pyplot as plt
# Figure 对象:创建画布
# figure( num,figsize,dpi,facecolor,edgecolor,frameon )
# num:图形编号或名称，取值为数字/字符串。
# figsize:绘图对象的宽和高，单位为英寸。
# dpi:绘图对象的分辨率，缺省值为80。
# facecolor:背景颜色。
# edgecolor:边框颜色。
# rameon:表示是否显示边框。
# plt.figure(num=1, figsize=(2, 2), facecolor="g", edgecolor="r", frameon=True)
# plt.plot()   绘制空白图形
# plt.show()

# subplot()函数——划分子图
# subplot( 行数, 列数, 子图序号 )
# plt.subplot(2, 2, 1)
# plt.subplot(2, 2, 2)
# plt.subplot(2, 2, 3)
# plt.subplot(2, 2, 4)
# plt.show()

# 设置中文字体
# plt.rcParams[" font.sans-serif"] = "SimHei"
# 恢复标准默认配置
# plt.rcdefaults()

# 添加标题
# 添加全局标题 suptitle (标题文字)
# 添加子标题 title (标题文字)

#  tight_layout()函数
# 检查坐标轴标签、刻度标签、和子图标题，自动调整子图，使之填充整个绘图区域，并消除子图之间的重叠。
# tight_layout( rect=[left, bottom, right, top])

# 查看系统可用字体
from matplotlib.font_manager import FontManager
fm = FontManager()
mat_fonts = set(f.name for f in fm.ttflist)
print(mat_fonts)

# mac下python matplotlib中文乱码解决方案
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
# plt.rcParams["font.family"] = "SimHei"
# 设置画布
plt.figure(facecolor="lightgrey")

# 绘制子图及其标题
plt.subplot(2, 2, 1)
plt.title("子标题01")
plt.subplot(2, 2, 2)
plt.title("子标题02", loc="left", color="blue")
plt.subplot(2, 2, 3)
myfontdict = {"fontsize": 12, "color": "g", "rotation": 30}
plt.title("子标题03", fontdict=myfontdict)
plt.subplot(2, 2, 4)
plt.title("子标题04", color="white", backgroundcolor="black")
# 设置全局标题
plt.suptitle("全局标题", fontsize=20, color="red", backgroundcolor="green")

# 自动调整子图布局
plt.tight_layout(rect=[0, 0, 1, 0.9])
plt.show()

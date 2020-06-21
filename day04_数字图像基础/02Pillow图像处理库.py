# Pillow图像处理库
# matplotlib.image :仅支持导入PNG格式的图像，且功能有限
# PIL(Python Imaging Library)：
# 功能丰富，简单易用
# 仅支持Python2.x版本, 且已经停止更新
# Pillow：
# 在PIL的基础上发展而成
# 支持Python 3

# 导入matplotlib.pyplot模块
import matplotlib.pyplot as plt
# 导入PIL.image模块
from PIL import Image
# 导入Numpy
import numpy as np
# /Users/a1/Documents/Projects/Python/day04_数字图像基础/test1.png
# 打开图像，返回image对象
img = Image.open("test1.png")
# 保存图像 图像对象.save("保存后的格式")
img.save("test1.tiff")
# 设置图像尺寸
plt.figure(figsize=(5, 5))
# 显示图像： plt.imshow(image对象/Numpy数组)
plt.imshow(img)
plt.title("test1.png")
# 显示绘图
plt.show()

# 设置图像属性
# 图像对象.format 设置图像格式
# 图像对象.size  设置图像尺寸
# 图像对象.mode  设置色彩模式

print("img格式:", img.format)
print("img尺寸：", img.size)
print("img色彩模式：", img.mode)

# 转化图像色彩模式
img_gray = img.convert("L")
print("mode=", img_gray)

# 绘制图像尺寸
plt.figure(figsize=(5, 5))
# 将img_gray显示到plt中
plt.imshow(img_gray)
# 显示plt
plt.show()

# 颜色通道的分离和合并
# 分离：图像对象.split()
# 合并：Image.merge(色彩模式,图像列表)
# 将img分离成R，G，B三种颜色通道
img_r, img_g, img_b = img.split()
# 绘制plt图像大小
plt.figure(figsize=(10,10))

# 绘制子图
plt.subplot(2, 2, 1)
# axis	获取或设置一些轴属性的便捷方法。
plt.axis("off")
# 将img_r显示在plt中
plt.imshow(img_r)  #cmap="gray":用灰度图表示颜色的亮度
# 设置该子图的标题
plt.title("R", fontsize=20)

plt.subplot(2, 2, 2)
# axis	获取或设置一些轴属性的便捷方法。
plt.axis("off")
# 将img_g显示在plt中
plt.imshow(img_g)  #cmap="gray":用灰度图表示颜色的亮度
# 设置该子图的标题
plt.title("G", fontsize=20)

plt.subplot(2, 2, 3)
# axis	获取或设置一些轴属性的便捷方法。
plt.axis("off")
# 将img_b显示在plt中
plt.imshow(img_b)  #cmap="gray":用灰度图表示颜色的亮度
# 设置该子图的标题
plt.title("B", fontsize=20)
# 显示 Plt
# plt.show()
# 将rgb合并
img_rgb = Image.merge("RGB", [img_r, img_g, img_b])
# 设置子图4
plt.subplot(2, 2, 4)
plt.axis("off")
plt.imshow(img_rgb)
plt.title("RGB", fontsize=20)
plt.show()

# 转化为数组
# np.array(图像对象)
# 将灰度图像转化为数组
arr_img_gray = np.array(img_gray)
print("shape:", arr_img_gray.shape)
print("arr_img_gray:", arr_img_gray)

# 将彩色图像转化为数组
arr_img = np.array(img)
print("img_shape:", arr_img.shape)
print("arr_img", arr_img)

# 如何取相反的颜色
# 255 -  灰度数组
arr_img_new = 255 - arr_img_gray
# 用plt绘制子图像
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(arr_img_gray, cmap="gray")

plt.subplot(122)
plt.imshow(arr_img_new, cmap="gray")
plt.show()

# 对图像进行缩放、旋转、镜像
# 缩放图像 ： 图像对象.resize((width,height))
# 绘制plt大小
plt.figure(figsize=(5, 5))
#
img_small = img.resize((64, 64))
plt.imshow(img_small)
plt.show()
img_small.save("image_resize.jpg")
# resize()方法不对原图进行修改，
# thumbnail()方法是原地操作，直接对image对象本身进行缩放。
# 图像对象.thumbnail((width, height)) 返回值是None


# 设置中文字体
plt.rcParams['font.sans-serif'] = "Arial Unicode MS"

# 旋转、镜像
# 图像对象.transpose(旋转方式)
# 设置plt大小
plt.figure(figsize=(10, 10))

# 设置子图1
plt.subplot(221)
plt.imshow(img)
plt.title("原图", fontsize=20)

plt.subplot(222)
# 将img对象的图片左右翻转
img_flr = img.transpose(Image.FLIP_LEFT_RIGHT)
plt.imshow(img_flr)
plt.title("左右翻转", fontsize=20)

plt.subplot(223)
# 将图片逆时针翻转270度
img_r270 = img.transpose(Image.ROTATE_270)
plt.imshow(img_r270)
plt.title("逆时针旋转270", fontsize=20)

plt.subplot(224)
# 将图片转置
img_tp = img.transpose(Image.TRANSPOSE)
plt.imshow(img_tp)
plt.title("转置", fontsize=20)

plt.show()

# 图像剪裁：在图像上指定的位置裁剪出一个矩形区域
# 图像对象.crop(x0,y0,x1,y1) x0,y0: 左上角  x1,y1: 右下角
# 返回值：图像对象
# 设置绘图大小
plt.figure(figsize=(10, 5))

plt.subplot(121)
plt.imshow(img)
# 图像剪裁
plt.subplot(122)
img_region = img.crop((200, 100, 800, 800))
plt.imshow(img_region)

plt.show()

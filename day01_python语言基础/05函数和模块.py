# 函数
#  实现某种特定功能的代码块
#  程序简洁，可重复调用、封装性好、便于共享
#  系统函数和用户自定义函数
# Python3.6.2版本，一共提供了68个内置函数。

# Python内置函数
#  数学运算函数:
# 1.返回x的绝对值  abs(x)
print(abs(-1))
# 2.返回x的y次幂 pow(x,y)
print(pow(2, 3))
# 3.返回浮点数x的四舍五入值，参数n 指定保留的小数位数，默认为0
print(round(3.1415, 2))
# 4.返回a除以b的商和余数，返回一个 元组。divmod(a,b)返回(a/b, a%b)
print(divmod(3, 5))

# 常用Python内置函数
print(len([1, 2, 3, 4]))  # 返回长度
print(max(1, 2, -1))
# sum(iterable[, start])
# iterable -- 可迭代对象，如：列表、元组、集合。
# start -- 指定相加的参数，如果没有设置这个值，默认为0。
print(sum([0, 1, 2, 3, 4], 2))  #0+1+2+3+4 +2=12
# 转变为字符串
str_1 = str({"myname": "dgx", "age": 12})
print(str_1, type(str_1))
# 转变为浮点型、整型、列表  float(),int(),list()
# 显示帮助信息 help()

print(dir(str_1))  # 显示属性

# 显示类型 type()
# 返回整型列表  range()
# 打开文件 open()
f = open("/Users/a1/Desktop/研究学习文件/TensorFlow2.0（神经网络）课件/{5}--第4讲Python语言基础（2）/{4}--4.4文件/file_test.txt")
print(f.read())
#  输入输出函数
#  类型转换函数
#  逻辑判断函数
#  序列操作函数
#  对象操作函数

# 用户自定义函数


# 一、输入函数：input (提示信息)
# 接收用户的输入，并以字符串类型返回
int_num = int(input("请输入一个数："))

# 二、输出函数:print(输出内容)
# 输出字符串常量、数学表达式、变量
print("Hello,Sir")
print(1+2)
int_x = 12
print(int_x)

# 格式化参数的使用
print("您输入的整数是：%d" %(int_num))

# 常用的格式化参数
# %c 格式化字符及其ASCII码
print("格式化的字符是%c" %('a'))
# %s 格式化字符串
print("格式化的字符串是%s" %('my name is Wechat'))
# %d 格式化整数
print("格式化的整数是%d" %(-12))
# %u 格式化无符号整型
print("格式化的无符号整型是%u" %(-12))
# %f 格式化浮点数字，可指定小数点后的精度
print("格式化的浮点数字是%.4f" %(-1.22))
# %e 用科学计数法格式化浮点数
print("科学计数法格式化浮点数是%e" %(-1.22))
# %p 用十六进制数格式化变量的地址
# print("用十六进制数格式化变量的地址是%p" %(0x70))
# 如果我们并不知道自己要打印的是什么类型的信息，这时可以用%r来表示
print("不知道类型的是%r" %(-1.22))

# 转义字符:
# 输出换行符 \n
print("纸上得来终觉浅，\n绝知此事要躬行")
# 输出引号 \"
print("输入双引号:\"")
# 输出 \\
print("输出反斜杠：\\")
# 失效转义字符 r R
print("C:\document\recent\num")
print(r"C:\document\recent\num")

# end参数  print(输出内容,end)
# 表示输出信息结束之后，附加的字符串
# 默认值是换行\n。
# 设置这个参数，可以改变输出效果
print("python")
print(3.7)
print("python", end=" ")
print(3.7)

# 三、format 格式化输出
# 1.常用方法 %
print("今天是%d年%d月%d日" %(2020, 5, 24))
# 2. 字符串的 format()方法
# 使用大括号“{}”代替“%”
# str.format( )
# 2.1基本用法:
# (1) 不带编号
print('{} {}'.format('hello', 'world'))
print("今年是{}年{}月{}日".format(2020, 5, 24))
# (2)带数字编号: 参数个数没有限制，可以多次使用，顺序可以任意放置
print("{0} {1} {0}".format("hello", "world"))
print("他叫{0}, 今年{1}岁，他朋友今年也{1}岁".format("lacy", '10'))
# (3)带关键字
print('他叫{name},今年{age}岁'.format(age=10, name='lacy'))
# 2.2 进阶用法

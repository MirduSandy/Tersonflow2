# 条件分支语句
# if-elif-else语句
x = int(input("X:"))
y = int(input("Y:"))
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")
print("continue...")


# 条件表达式 : 表达式1(条件为真的结果) if 判断条件 else 表达式2( 条件为假的结果)
print(x if x > y else y)

# 循环语句
# while 语句
#  while 循环条件 :
#     循环体
# 死循环:循环条件始终为真,一直无法满足退出循环的条件
i = 1
sum = 0
while i < 101:
    sum += i
    i += 1
print(sum)

# for语句
# for 标识符 in 可迭代对象:
#       循环体
for i in "Python":
    print(i, end=" ")
print()

# range()函数
# range ( 起始数字, 结束数字, 步长 )
# 前闭后开:整数序列中不包括结束数字
# 起始数字省略时，默认从0开始
# 步长省略时，默认为1
for i in range(1, 10, 2):
    print(i, end=" ")
print()
int_sum = 0
for i in range(101):
    int_sum += i
print("int_sum=", int_sum)

# continue语句:终止本次循环，开始下一次循环
# 计算1-100之间的所有奇数的和
int_sum1 = 0
for i in range(1, 101):
    if i % 2 == 0:
        continue
    int_sum1 += i
print("int_sum1=", int_sum1)

# 或者：
int_sum2 = 0
for i in range(1, 101, 2):
    int_sum2 += i
print("int_sum2=", int_sum2)

# break语句:跳出循环体，结束循环
int_i = 1
int_sum3 = 0
while int_i < 101:
    if int_sum3 <= 3000:
        int_sum3 += int_i
        int_i += 1
    else:
         break
print("int_sum3=", int_sum3)

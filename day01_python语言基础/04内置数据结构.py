# 序列数据结构(sequence)
#  成员是有序排列的
#  每个元素的位置称为下标或索引  通过索引访问序列中的成员
#  Python中的序列数据类型有字符串、列表、元组 "abc" ≠ "bca"
#  Python中的列表和元组，可以存放不同类型的数据
#  列表使用方括号[ ]表示，元组使用小括号( )表示。
# 列表:[1,2,3] 元组: (1,2,3)

# 列表(list): 内容是可以改变的，append()、insert()
lst_1 = [1, 2, 3]
lst_2 = [4]
lst_3 = [[1, 2, 3], [4, 5, 6]]
lst_mix = [160612, "张明", 18, [92, 76, 85]]
lst_empty = [ ]
print(lst_mix)

# 元组(tuple): 一经定义，元组的内容不能改变
t1 = (1)        # 整型 <class 'int'>
tup_2 = (1,)    # 元组 <class 'tuple'>
print("t1=", t1, type(t1))
print("tup_2=", tup_2, type(tup_2))

# 索引(下标):通过它访问序列中的元素
# 1.字符串索引
str_py = "Python"
# 遍历列表中的元素
for i in str_py:
    print(i, end=" ")
print()
print(str_py[0])
# 逆向索引
print(str_py[-1])

# 2.列表索引
lst_4 = ["p", 2, 3]
print(lst_4[0])
# 逆向索引
print(lst_4[-1])

# 切片:一次性从序列中获取多个元素
# [开始位置:结束位置] 前闭后开: 切片不包括结束位置的元素
print(str_py[1:5])
print(lst_4[:2])

# 获取序列的长度——len(序列名称)
print(len(str_py))

# 更新列表 ——向列表中添加元素
# 向列表中追加元素  append（）
lst_1.append(4)
print(lst_1)
# 向列表中追加元素 insert()
lst_1.insert(1, 5)
print(lst_1)
#
lst_1.pop(3)
print(lst_1)

# 更新列表——合并列表  extend()
lst_6 = [1, 2, 3]
lst_7 = [4]
lst_6.extend(lst_7)
print("extend()后lst_6=", lst_6)

# "+" 运算符
lst_8 = lst_6 + lst_7
print("+后lst_8=", lst_8)


#  更新列表——删除列表中的元素 del 语句
del lst_8[4]
print("del后的lst_8=", lst_8)

# 更新列表——排序
#  sort() :对列表中的元素排序
#  reverse():对列表中的元素倒排序
lst_8.sort()
print("sort()后的lst_8=", lst_8)
lst_8.reverse()
print("reverse()后的lst_8=", lst_8)

# 字典和集合
#  字典(Dictionary)
#  每个字典元素都是一个键/值对(key/value)  键:关键字
#  值:关键字对应的取值
# 创建字典
dic_score = {"语文": 80, "数学": 83, "英语": 78, "体育": 80}
dic_employ = {"name": "Mary", "age": 26}
dic_employ = {"name": {"first": "Mary", "last": "Smith"}, "age": 26}
# 打印字典、访问字典中的元素
print(dic_score)
print(dic_employ["name"]["first"])
# 判断字典是否存在元素——in运算符
print("name" in dic_employ)
print("语文" not in dic_score)

# 遍历字典元素
#  keys():返回字典中所有的关键字
#  values():返回字典中所有的值
#  items():返回字典中所有的键值对
# 遍历字典中所有的键
# 字典中的元素是无序的，因此每次显示的顺序可能不同
for i in dic_score.keys():
    print(i, end=" ")
print()
for i in dic_score.values():
    print(i, end=" ")
print()
for i in dic_score.items():
    print(i, end=" ")
print()

#  更新字典:添加元素、修改指定元素的取值
dic_score["语文"] = 100
print(dic_score)
print(dic_score.keys())

# 合并字典:将另一个字典中的元素追加到字典中
dic_student = {"name": "Mary", "age": 23}
dic_contact = {"tel": 17805593657, "email": "xin123333@qq.com"}
dic_student.update(dic_contact)
print(dic_student)

# 删除字典中的元素
# pop (指定元素的关键字) 删除字典中的指定元素
# clear() 清空字典中的所有元素
# 另外，Python中还提供了了del语句，使用它可以删除字典中 指定的元素，或删除字典本身。
dic_student.pop("email")


#  集合(set):由一组无序排列的元素组成。
#  可变集合(set):创建后可以添加、修改和删除其中的元素
#  不可变集合(frozenset):创建后就不能再改变了 {1,2,3,4,5,4,5}

# 创建集合
set_1 = {1, 2, 3, 4, 5, 1}     #Python会自动的将集合中重复的素清理掉
print(set_1)
print(len(set_1))
tru_1 = (1, 2, 3, 4, 5, 1)
print(tru_1)
print(tru_1.__len__())
lst_1 = [1, 2, 3, 4, 5, 1]
print(lst_1)
print(lst_1.__len__())
dic_1 = {1, 2, 3, 4, 5, 1}
print(dic_1)
print(dic_1.__len__())

# set() 创建可变集合
# frozenset() 创建不可变集合
set_2 = set("Python")
print(set_2)
set_3 = frozenset("Python")
print(set_3)

#  集合中的元素是无序的，因此不能通过下标来访问
#  打印集合、获取集合长度、遍历集合的方法，与其他内置数据类型类似
print(set_3)
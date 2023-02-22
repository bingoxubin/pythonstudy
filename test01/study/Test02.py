# 字符串str
str = 'hello'
str = "hello"
str = '''hello'''
# 索引 0,1,2,3,4
# 负索引 -5,-4,-3,-2,-1
print(str[0])  # h
print(str[-1])  # o
print(str[len(str) - 1])
# 切片
print(str[1:3])  # el  起始：结束不包含：步长    如果起始是开始，或者结束是最后，都可以省略
# 步长为正数 从左往右截取   步长为负数 从右往左截取
print(str[-2:-5:-1])  # lle   此时如果步长为1 那么返回空
# 倒着获取数据
print(str[::-1])
# 字符串常见操作
print(str.find("llo", 0, 5))
print(dir(str))  # 查看str有哪些方法
# 遍历
for value in range(0, len(str)):
    print(str[value])
for value in str:
    print(value)
for index, value in enumerate(str):
    print(index, value)
# 判断元素是否是可迭代类型
from collections import Iterable

print(isinstance("123", Iterable))

# 列表list
list1 = ["hello", "world", 1, 3]
print(list1, len(list1), type(list1), list1[3])
# 切片
print(list1[1:3])
# 列表的增删改查
list2 = []  # 定义一个空列表
list2.append(1)  # 追加数据
list2.insert(1, "def")  # 指定位置插入
print(list2)  # [1, 'def']
list1.extend(list2)
print(list1)  # ['hello', 'world', 1, 3, 1, 'def']   合并两个列表  注意区别于list1.append(list2),是将list2作为元素追加到list1
list1[1] = 2  # 修改
list1.remove('def')  # 删除
del list1[0]  # 根据下标进行删除
list1.pop()  # 删除最后一个元素  pop(0) 删除0位置的元素
print(list1)  # [2, 1, 3]
list1.clear()  # 清空列表
# 遍历
print("==============", list2)
for value in list2:
    print(value)
for index, value in enumerate(list2):
    print(index, value)
for value in range(0, len(list2)):
    print(list2[value])
print(list2.count(1))  # 指定数据在列表中的个数

# 元祖tuple
# 另一种有序列表叫元组，tuple和list非常类似，但是tuple一旦初始化就不能修改
tuple1 = ('Michael', 'Bob', 'Tracy')
print(tuple1, type(tuple1), tuple1[0])
# 这个tuple没有append(),insert()这样的方法，其他获取元素的方法和list一样，因为tuple不可变，所以代码更安全，能用tuple代替list就尽量用tuple
# 注意：如果元组中的元素是一个列表，那么列表中的值是可以修改的
tuple3 = (1, [1, 2])
tuple3[1][0] = 2
print(tuple3)  # (1, [2, 2])
tuple2 = (1,)  # 如果元组中只有一个元素，需要加逗号，否则表示一个优先级括号的运算符

# 字典dict
# 字典的每个键值对用：分割，每个对之间用,号分割，整个字典包括在花括号{}中
dict1 = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(dict1, type(dict1), len(dict1))
print(dict1['Michael'])  # 获取值，如果没有报错
print(dict1.get('Michael'))  # 获取值，如果没有，None
my_dict = {}
my_dict['name'] = 'zs'  # 添加
my_dict['name'] = 'ls'  # 修改
my_dict['age'] = 18
print(my_dict)
# del my_dict['name']  # 删除
print(my_dict.pop('name'))  # 删除   有返回值
# my_dict.clear()  # 清空
print('name' in my_dict)  # 判断有没有这个key
print('name' in my_dict.keys())  # 判断有没有这个key
my_dict.values()  # 获取所有的values值
my_dict.items()  # 以列表的形式取出数据，并且列表中的元素是元组
print(my_dict)
# 遍历
for key in my_dict:
    print(key)
    print(my_dict[key])
for key, value in my_dict.items():
    print(key, value)
for value in my_dict.keys():
    print(value, my_dict[value])
# 注意：字典中key必须是不可变类型 () str int

# 集合set
# 集合是一个无序的不重复元素序列，可以使用{}或者set()函数创建集合
# 注意：创建一个空集合必须用set()而不是{}，因为{}是用来创建一个空字典
my_set = {1, 3, 'abc', 'hello'}
print(my_set, type(my_set))
my_set.add(2)  # 添加元素
print(my_set)
my_set = set()  # 创建空的集合
# 集合列表转换，去重
list1 = [1, 1, 3, 5, 3]
set1 = set(list1)
print(set1)
list2 = list(set1)
print(list2)
# 遍历
for value in set1:
    print(value)
for index, value in enumerate(set1):
    print(index, value)
# 字典和集合都是无序的，没有索引

# 1、注释
'''多行代码注释'''
"""多行代码注释"""

# 2、变量：存储程序数据的容器
score = 100
print(score)
# 通过type查看变量类型
print(type(score))
is_ok = True
print(type(is_ok))
# 常用的数据类型int,str,float,bool,list,tuple,dict,set

# 3、关键字
# ['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally',
# 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
import keyword

print(keyword.kwlist)

# 4、数据类型转换
num = 10
my_str = str(num)
print(my_str)
# int(x) 转为int
# float(x)
# complex(real,imag) 复数
# str(x)
# repr(x) 对象转为表达式字符串
# eval(str) 计算字符串中的有效python表达式
# tuple(s) 转为元组
# list(s) 转为列表
# chr(x) 整数转为Unicode字符
# prd(x) 字符转为ascii整数
# hex(x) 整数转16进制
# oct(x) 整数转8进制
# bin(x) 整数转2进制

# 5、输入输出
print('hello world')
print('hello', 'world')
str1 = 'hello'
str2 = 'world'
print(str1, str2, sep='……')
# 默认有一个换行符 \n
print('hello', end='')
print('world')
# 格式化输出 格式化符号
# %s 输出字符串
# %d 输出int类型数字
# %f 输出浮点数   print('%.1f'%3.14)  保留一位小数
# %x 输出16进制数
name = 'zs'
age = 10
print('我叫%s,年龄%d' % (name, age))
# format格式化函数
print('我叫{},年龄{}'.format(name, age))
print('我叫{na},年龄{ag}'.format(na=name, ag=age))
print('我叫{0},年龄{1}'.format(name, age))
# 输入
# str3 = input('请输入')
# print(str3)
# str4 = input('请输入'),split(',')

# 6、判断python的版本
from sys import version_info

# version = version_info.major
print(version_info.major)

# 7、python运算符
'''
+ - * /
//取整除
% 取余
** 指数
= 赋值
+= -= *= /= %= **= //=取整除赋值
'''

# 8、逻辑判断
# 比较运算符 ==，>=,>,<,<=,!=  结果：True,False
# 逻辑运算符 and：与   or：或   not：取反
# 优先级 not > and > or
print(True or True and False)
print(not True and False)
a = 10
if a == 10:
    print("success")
elif a == 20:
    print("or")
else:
    print("false")

# 9、循环
flag = 10
while flag > 0:
    print(flag)
    flag -= 1

for value in range(1, 6):
    print(value)
for value in range(10, 1, -1):
    print(value)
print(list(range(1, 6)))  # [1, 2, 3, 4, 5]
print(list(range(1, 10, 2)))  # [1, 3, 5, 7, 9]

'''
1*1 = 1
1*2 = 2 2*2 =4
1*3 = 3 2*3 = 6 3*3 = 9
'''
for i in range(1, 10):
    for j in range(1, i + 1):
        print("{}*{}={}".format(i, j, i * j), end=" ")
    print()
# break continue
value = 1
while value <= 5:
    if value == 4:
        value += 1
        # continue
        break
    print(value, end=" ")
    value += 1

# 异常
# print(num)
# print(1)
try:
    print(1)
    print("有问题的代码放到这里")
except Exception as e:
    print(e)

print(1)

try:
    print('try……')
    r = 10 / int('a')
    print('result:', r)
except ValueError as e:
    print("ValueError", e)
except ZeroDivisionError as e:
    print("ZeroDivisionError", e)
finally:
    print('finally')
print('END')

# 模块
# 通俗理解就是一个.py文件就是一个模块，模块是管理功能代码的
# 内置模块：就是python自己内部自带的不需要我们去下载的模块，比如：time,random等
# 注意：自定义模块名字和变量名的定义很类似，都是由字母、数字、下划线组成，但是不能以数字开头，否则无法导入该模块
# help('modules')   查看已经安装的模块

# 模块导入
# 1、import 直接导入
# import First_Module
# import First_Module as first #给模块起名字
#
# print(__name__)  # __main__
# First_Module.show()

# 2、从某个模块中导入某个方法
# from First_Module import show
# from First_Module import show, show1  # 导入一个模块的多个方法
# from First_Module import *  # 导入一个模块的多个方法
# show()

# 3、给模块中的方法重命名
# from first_module import show as first_show
# from second_module import show as second_show

# 包
# 模块是一个.py文件
# 包是一个装有多个.py文件的文件夹
# 通俗理解包就是一个文件夹，只不过文件夹里面有一个init.py文件，包是管理模块的，模块是管理功能代码的
# 比如first_package文件夹下面包含了，__init__py文件，first.py文件，second.py文件

# import导入包里面的模块
# import first_package.first
# import导入包里面的模块设置别名
# import first_package。first as one
# from 导入报名 import导入模块名
# from first_package import second
# from 包名.模块名 import功能代码
# from first_package.first import show



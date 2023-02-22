# 1、pandas
# Pandas是基于NumPy的一种工具，该工具是为了解决数据分析任务而创建的。Pandas纳入了大量库和一些标准的数据模型
# 提供了高效的操作大型数据集所需的工具。pandas提供了大量能使我们快速便捷的处理数据的函数和方法
# numpy中数据类型都是一致的，pandas不需要这样

# pandas基于两种数据类型：series与dataFrame
'''
series是pandas中最基本的对象，series类似一种一维数组，事实上，series基本上就是基于numpy的数组对象来的，
和numpy的数组不同，series能为数据自定义标签，也就是索引（index),然后通过索引来访问数组中的数据
dataframe是一个二维的表结构。pandas的dataframe可以存储许多种不同的数据类型，并且每一个坐标轴都有
自己的标签，可以把它想象成一个series的字典项
'''

# 2、Series对象
import pandas as pd
from pandas import Series, DataFrame
import numpy as np

sel = Series([1, 2, 3, 4])
print(sel)
sel = Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
print(sel)
'''
0    1
1    2
2    3
3    4
dtype: int64
'''
print(sel.values)
print(sel.index)
print(list(sel.iteritems()))
'''
[1 2 3 4]
Index(['a', 'b', 'c', 'd'], dtype='object')
[('a', 1), ('b', 2), ('c', 3), ('d', 4)]
'''

# 将字典转为series
dict = {"red": 100, "black": 400, "green": 300, "pink": 900}
sel3 = Series(dict)
print(sel3)

# series数据获取
sel = Series(data=[1, 2, 3, 4], index=list('abcd'))
print(sel)
print("索引下标", sel['c'])
print("位置下标", sel[2])
# 获取不连续的数据
print('索引下标', sel[['a', 'c']])
print('位置下标', sel[[1, 3]])
# 可以使用切片获取数据
print('位置切片', sel[1:3])  # 左包含右不包含
print('索引切片', sel['b':'d'])  # 左右都包含
'''
位置切片 b    2
c    3
索引切片 b    2
c    3
d    4
'''

# 3、DataFrame的创建
'''
dataframe(数据表）是一种二维数据结构，数据以表格的形式存储，分成若干行和列，通过dataframe，能很方便的处理数据，常见的操作比如选取、替换行或列的数据，还能重组数据表、
修改索引、多重删选等。我们基本上可以把dataframe理解成一组采用同样索引的series的集合。
调用dataframe（）可以将多重格式的数据转换为dataframe对象，它的三个参数data、index和columns分别为数据、行索引、和列索引
'''

# 4、数据处理

# 5、数据合并

# 6、多层索引

# 7、时间序列

# 8、分组聚合

# 9、分组案例

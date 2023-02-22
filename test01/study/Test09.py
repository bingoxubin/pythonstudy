# numpy
'''
numpy(Numerical Python)是一个开源的python科学计算库，用于快速处理任意维度的数组
numpy支持常见的数组和矩阵操作，对于同样的数值计算任务，使用numpy比直接使用python要简洁的多
numpy使用ndarray对象来处理多维数组，该对象是一个快速而灵活的大数据容器
'''

# 普通列表和numpy的效率对比
import random
import time
import numpy as np

# a = []
# for i in range(100000000):
#     a.append(random.random())
#
# t1 = time.time()
# sum1 = sum(a)
# t2 = time.time()
#
# b = np.array(a)
# t4 = time.time()
# sum3 = np.sum(b)
# t5 = time.time()
# print(t2 - t1, t5 - t4)  # 0.3720371723175049 0.10571765899658203

# NumPy的Ndarray对象
list1 = [1, 2, 3, 4]
oneArray = np.array(list1)
# 数组
print(type(oneArray))  # <class 'numpy.ndarray'>
print(oneArray)  # [1 2 3 4]  跟列表的区别，中间没有逗号

# 创建一维数组的多种形式
# 1.直接传入列表的方式
t1 = np.array([1, 2, 3])
print(t1, type(t1))
# 2.传入range生成序列
t2 = np.array(range(10))
print(t2, type(t2))
# 3.使用numpy自带的np.arange()生成数组
t3 = np.arange(0, 10, 2)
print(t3, type(t3))

# 创建二维数组的多种形式
list2 = [[1, 2], [3, 4], [5, 6]]
twoArray = np.array(list2)
print(twoArray, type(twoArray))
'''[[1 2]
 [3 4]
 [5 6]] <class 'numpy.ndarray'>'''
print(twoArray.ndim)  # 维度 2
print(twoArray.shape)  # 查看几行几列  (3, 2)
print(twoArray.size)  # 6 多少个数据
print(twoArray[1][0])  # 3

# 调整形状
four = np.array([[1, 2, 3], [4, 5, 6]])
print(four)
'''
[[1 2 3]
 [4 5 6]]
 '''
# four.shape = (3,2) #此种方式修改原有的数组
# print(four)
'''
[[1 2]
 [3 4]
 [5 6]]
 '''
five = four.reshape(3, 2)  # 返回一个新的数组
print(five)
print(four)
'''
[[1 2]
 [3 4]
 [5 6]]
[[1 2 3]
 [4 5 6]]
'''

# 将多维变成一维
five = four.reshape((6,), order='F')  # C表示横向取   F表示列向取
six = four.flatten(order='F')
print(five)
print(four)

# 数组转list
a = np.array([9, 12, 88, 14, 25])
list_a = a.tolist()
print(list_a, type(list_a))

# 数据类型
f = np.array([1, 2, 3, 4, 5], dtype=np.int16)
print(f.dtype, f.itemsize)
# 调整数据类型
f1 = f.astype(np.int64)
print(f1.dtype)
# 随机生成小数，保留两位
print(round(random.random(), 2))  # 0.19
arr = np.array([random.random() for i in range(10)])
print(arr)
# [0.02027637 0.75997195 0.19789717 0.25936591 0.10050215 0.88726512 0.17775365 0.51179134 0.26095569 0.71643455]
print(np.round(arr, 2))  # [0.02 0.76 0.2  0.26 0.1  0.89 0.18 0.51 0.26 0.72]

# 数组的计算
# 数组和数之间的计算
t1 = np.arange(24).reshape((6, 4))
print(t1)
'''
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]
 [12 13 14 15]
 [16 17 18 19]
 [20 21 22 23]]
'''
print(t1 + 2)
'''
[[ 2  3  4  5]
 [ 6  7  8  9]
 [10 11 12 13]
 [14 15 16 17]
 [18 19 20 21]
 [22 23 24 25]]
'''
# 数组和数组之间的计算
'''
同种形状的数组对应位置进行计算
不同形状的多维数组不能计算
'''
t1 = np.arange(24).reshape((6, 4))
t2 = np.arange(100, 124).reshape((6, 4))
print(t2 - t1)

# 注意：
t1 = np.arange(24).reshape((4, 6))
t2 = np.arange(0, 6)
print(t1, t2, t1 - t2)
'''
[[ 0  1  2  3  4  5]
 [ 6  7  8  9 10 11]
 [12 13 14 15 16 17]
 [18 19 20 21 22 23]] 
 
 [0 1 2 3 4 5]

[[ 0  0  0  0  0  0]
 [ 6  6  6  6  6  6]
 [12 12 12 12 12 12]
 [18 18 18 18 18 18]]
'''

# 数组中的轴
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a)
print(np.sum(a, axis=0))
print(np.sum(a, axis=1))
'''
[[1 2 3]
 [4 5 6]]
 
[5 7 9]

[ 6 15]
'''
# 三维数组
a = np.arange(27).reshape((3, 3, 3))
print(a)
'''
[[[ 0  1  2]
  [ 3  4  5]
  [ 6  7  8]]

 [[ 9 10 11]
  [12 13 14]
  [15 16 17]]

 [[18 19 20]
  [21 22 23]
  [24 25 26]]]

'''

# 数组的索引和切片
a = np.arange(10)
print(a[2:7:2])  # [2 4 6]
print(a[2])
print(a[2:])

t1 = np.arange(24).reshape(4, 6)
print(t1)
print('*' * 20)
print(t1[1])  # 取一行
print(t1[1:3, :])  # 连续的多行
print(t1[[0, 2, 3], :])  # 不连续的多行
print(t1[:, 1])  # 取一列
print(t1[:, 1:])  # 连续的多列
print(t1[:, [0, 2, 3]])  # 不连续的多列
print(t1[2, 3])  # 取某一个元素
print(t1[[0, 1, 2], [0, 1, 3]])  # 取多个元素

# 数组中的数值修改
t = np.arange(24).reshape(4, 6)
t[1, :] = 0  # 修改某一行的值
t[:, 1] = 0  # 修改某一列的值
t[1:3, :] = 0  # 修改连续多行
t[:, 1:4] = 0  # 修改连续多列
t[1:4, 2:5] = 0  # 修改多行多列
t[[0, 1], [0, 3]] = 0  # 修改多个不相邻的点
t[t < 10] = 0  # 根据条件修改，小于10的值修改掉
t[(t > 2) & (t < 6)] = 0  # 与
t[(t < 2) | (t > 6)] = 0  # 或
t[~(t > 6)] = 0  # 非

score = np.array([[80, 88], [82, 81], [75, 81]])
result = np.where(score > 80, True, False)
print(result)

# 数组的添加、删除、去重
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a)
print(np.append(a, [7, 8, 9]))
print(np.append(a, [[7, 8, 9]], axis=0))  # 沿0轴添加
print(np.append(a, [[5, 5, 5], [7, 8, 9]], axis=1))  # 沿1轴添加
'''
[[1 2 3]
 [4 5 6]
 [7 8 9]]
 
[[1 2 3 5 5 5]
 [4 5 6 7 8 9]]
'''
# 插入 insert
# 删除 delete
# 去重 unique
# np.append()  两个数组之间拼接
# np.concatenate() 多个数组的拼接

# nan 空值
# inf 无穷大
a = np.nan
b = np.inf
print(a, type(a))
print(b, type(b))
'''
nan <class 'float'>
inf <class 'float'>
'''
t = np.arange(24, dtype=float).reshape(4, 6)
t[3, 4] = np.nan
t[np.isnan(t)] = 0
print(t)
print(np.nan == np.nan)  # False  任意两个nan值是不同的
# 空值的个数
print(np.count_nonzero(t != t))

# 处理空值的方式
t = np.arange(24).reshape(4, 6).astype('float')
t[1, 3:] = np.nan
print(t)
# 遍历每一列，然后判断每一列是否有nan
for i in range(t.shape[1]):
    # 获取当前列数据
    temp_col = t[:, i]
    # 判断当前列的数据中是否含有nan
    nan_num = np.count_nonzero(temp_col != temp_col)
    if nan_num != 0:  # 条件成立说明含有nan
        # 将这一列不为nan的数据拿出来
        temp_col_not_nan = temp_col[temp_col == temp_col]
        # 将nan替换成这一列的平均值
        temp_col[np.isnan(temp_col)] = np.mean(temp_col_not_nan)
print(t)

# 二维数组的转置
a = np.arange(12).reshape(3,4)
print('原数组')
print(a)
print('\n')

print('对换数组：')
print(np.transpose(a))
# 或者用如下方法
print(a.T)
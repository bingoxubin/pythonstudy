# 文件
# 文件包括文本文件和二进制文件（声音、图像、视频）
# 二进制读写是将内存里面的数据直接读写入文本中
# 而，文本，则是将数据先转换成字符串，再写入到文件中

# f = open('1.txt','r')
# 读取或者写入操作
# f.close()

'''
r：只读，文件如果不存在就会报错
w：只写，会将原来的数据清空，再写入，如果文件不存在，会创建一个新的文件
a：追加写入
rb：以二进制的形式读取
wb：以二进制的形式写入
ab：以二进制的形式追加写入文件
r+：可读可写的操作，覆盖的形式写入  开始：ABC 写入：DE  结果：DEC
'''

# w模式
file = open('./source/1.txt', 'w', encoding="utf-8")
print(file.encoding)  # utf-8
# 写入数据
file.write('a')
file.write('b')
file.close()

# r模式
file = open('./source/1.txt', 'r', encoding="utf-8")
content = file.read()
print(content)  # ab
file.close()

# a模式
file = open('./source/1.txt', 'a', encoding="utf-8")
file.write('哈哈')
file.close()

# rb二进制形式读取数据
file = open('./source/1.txt', 'rb')
content = file.read()
print(content)  # b'ab\xe5\x93\x88\xe5\x93\x88'
# 解码
result = content.decode('utf-8')
print(result)  # ab哈哈
# 编码
print(result.encode('utf-8'))  # b'ab\xe5\x93\x88\xe5\x93\x88'
file.close()

# r+读写
file = open('./source/1.txt', 'r+', encoding="utf-8")
file.write('cd')
file.close()

file = open('./source/1.txt', 'r+', encoding="utf-8")
result = file.read()
print(result)  # cd哈哈
file.close()

# 文件的不同读取方式
file = open('./source/1.txt', 'r', encoding='utf-8')
print(file.read(4))  # cd哈哈 如果是r这种方式，以字符为单位，英文占一个字节，中文占三个字节
file.close()

file = open('./source/1.txt', 'rb')
print(file.read(4))  # b'cd\xe5\x93',如果是rb这种方式，是以字节的个数为单位的
file.close()

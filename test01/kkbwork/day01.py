
#定义一个字符串处理函数, 该函数需要提供字符串切割功能, 并且需要将切割之后的类型处理为[(str1,1),(str2,1),(str3,1)]这种类型返回
str = "life is short please use python life is short"
result = str.split(" ")
list2 = []
for temp in result:
    list1 = []
    list1.append(temp)
    list1.append(1)
    tuple1 = tuple(list1)
    list2.append(tuple1)
print(list2)

last = list([(s,1) for s in str.split(" ")])
print(last)


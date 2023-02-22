# 题目一：
# 判断数字是否被2 3整除
# value = input("input nums")
# if int(value) % 2 == 0 and int(value) % 3 == 0:
#     print("能同时被2和3整除")
# elif int(value) % 2 == 0:
#     print("能被2整除")
# elif int(value) % 3 == 0:
#     print("能被3整除")
# else:
#     print("不能被2 被3 整除")

# 题目二：
# seven 123登陆成功，否则有三次机会
# for value in range(1,4):
#     name = input("请输入用户名密码")
#     list = name.split(",")
#     if list[0] == "seven" and int(list[1]) == 123 :
#         print("登陆成功")
#         break
#     else:
#         print("登陆失败！用户名密码不正确")

# 题目三：
# 1-2+3-4+5-6+99
# result = 0
# for value in range(1, 100):
#     if value % 2 == 1:
#         result += value
#     else:
#         result -= value
# print("result的值为{}".format(result))

# 题目四：
# 用for和while打印乘法表
# for的方式
# for i in range(1,10):
#     for j in range(1,i+1):
#         print("%d*%d=%d"%(i,j,i*j),end=" ")
#     print()
# while的方式
# i = 1
# while i < 10:
#     j = 1
#     while j <= i:
#         print("%d*%d=%d" % (i, j, i * j), end=" ")
#         j += 1
#     i += 1
#     print()

# 题目五
# 1,2,3,4能组成多少个互不相同且不重复的三位数
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if i != j and i != k and j != k:
                print("%d"%(100*i+10*j+k),end=" ")

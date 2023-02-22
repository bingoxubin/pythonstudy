# 函数
# 把具有独立功能的代码块组织为一个小模块，这就是函数
# 定义
def fun():
    print("hello")

# 调用
fun()

# 函数常见类型,方法名不能跟变量名重名
def show(name, age):
    print("name:%s,age:%d" % (name, age))

show("zs", 18)

def show1():
    name = 'zs'
    return name

print(show1())

def count(num1, num2):
    num = num1 + num2
    return num

print(count(1, 2))

# 函数的参数
def sum_num(num1, num2):
    result = num1 + num2
    print("%d,%d" % (num1, num2))
    return result

print(sum_num(num2=1, num1=4))  # 4,1

def sum_num(num1, num2=1):  # 缺省参数,如果没有该参数，使用默认值
    # 注意：如果函数的第一个参数设置为缺省的，后面的参数都得是缺省的
    result = num1 + num2
    return result

print(sum_num(1))  # 2

# 不定长位置参数
def show(*args):
    print(args, type(args))
    sum = 0
    for value in args:
        sum += value
    return sum

print(show(1, 2, 3, 4))

# 不定长关键字参数
def show(**keyargs):
    print(keyargs, type(keyargs))
    for key, value in keyargs.items():
        print(key, value)

show(name='zs', age=18)

# 定义函数标准格式
def show(name, age, high=180, *args, **keyagrs):
    pass

# 函数的返回值
def show(num1, num2):
    return num1, num2

print(show(1, 2))

# 递归函数
# 递归实现费布那齐数列 1 1 2 3 5 8 13 21
def show(nums):
    if nums == 1 or nums == 2:
        return 1
    else:
        return show(nums - 1) + show(nums - 2)

print(show(8))

# 实现5！
def show(nums):
    if nums == 1:
        return 1
    else:
        return nums * show(nums - 1)

print(show(6))

# 局部变量和全局变量
# 在函数里面定义的变量就是局部变量，外面就是全局变量
age = 20

def show():
    global age  # 修改全局变量,函数想要修改全局变量的值的时候使用
    age = 18
    print(age)

show()
print(age)
# 注意：作用域只有函数才有的
for value in range(1, 5):
    print(value)
print(value + 3)  # 可以执行

value = 0

def show():
    global value
    for i in range(1, 10):
        value = value + i
    return value

print(show())

i = 1

def show():
    # i = i + 1  #报错，函数中局部变量，先定义一个跟全局变量重名的i，然后进行i+1，此时i找不到值，所以报错
    a = i + 1  # 不报错，定义一个局部变量a，此时执行i+1，i在局部变量中找不到，所以找全局变量为1

show()

# 函数案例
# 随机生成电话号码
import random
def createTelNum():
    second = [3, 4, 5, 7, 8][random.randint(0, 4)]
    third = {
        3: random.randint(0, 9),
        4: [5, 7][random.randint(0, 1)],
        5: [i for i in range(0, 10) if i != 4][random.randint(0, 8)],
        7: [6, 7, 8][random.randint(0, 2)],
        8: random.randint(0, 9)
    }[second]
    laststr = ''
    for value in range(8):
        laststr = laststr + str(random.randint(0, 9))
    return "1{}{}{}".format(second,third,laststr)
print(createTelNum())

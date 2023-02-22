# 面向对象
# 面向过程和面向对象，比如做五子棋的一个游戏，那么面向过程一步一步描述不能出错，先开始，画棋盘，下子，再画棋盘
# 面向对象编程的2个非常重要的概念：类和对象
# 对象是面向对象编程的核心，在使用对象的过程中，为了将具有共同特征和行为的一组对象抽象定义，提出了另外一个类
# 类就相当于制造飞机时的图纸，用它来进行创建的飞机就相当于对象

# 定义一个类，然后根据类去创建对象
class Teacher(object):
    # 方法 self谁调用了这个方法，self就是谁
    def show(self):
        print("泡脚")

# 根据类创建对象
teacher = Teacher()
teacher.show()

class Dog(object):
    def eat(self):
        print("{}:eat".format(self.name))

dog1 = Dog()
dog1.name = 'tom'  # 添加属性
dog1.age = 18
print(dog1.name, dog1.age)
dog1.eat()  # 方法

dog2 = Dog()
dog2.name = 'jim'
dog2.eat()

# 定义类的时候设定属性
class Teacher(object):
    # 初始化方法
    def __init__(self, name, age):
        # 默认属性
        self.name = name
        self.age = age

    def show(self):
        print(self.name, self.age)

t1 = Teacher('kkb', 18)
t1.show()
print(t1.name, t1.age)
t2 = Teacher('hello', 20)
print(t2.name, t2.age)

# 对象的创建流程
class Dog(object):
    # 初始化
    def __init__(self):
        print("__init__")

    # 对象创建
    def __new__(cls):
        print('__new__')
        return object.__new__(cls)

Dog()  # __new__  __init__

# 继承
# 单继承
class Person(object):
    def __init__(self):
        self.name = "zs"
        self.age = 19

    def show(self):
        print("======" + self.name, self.age)

class Stuednt(Person):
    pass

student = Stuednt()
student.show()
print(student.name)
print(student.age)

# 多继承
class A(object):
    def show(self):
        print("A")

class B(object):
    def show(self):
        print("B")

class C(A, B):
    pass

c = C()
c.show()
print(C.mro())  # 打印继承链  [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]

class D(object):
    def showD(self):
        print("D")

class E(D):
    def showE(self):
        print("E")

class F(E):
    def showF(self):
        print("F")

f = F()
f.showD()  # D

# 私有属性
class Person(object):
    def __init__(self):
        # 实例属性，公开的
        self.name = 'zs'
        # 私有属性,只能在类的内部使用
        self.__age = 18

    def set_age(self, new_age):
        if (new_age > 0 and new_age <= 100):
            self.__age = new_age
        else:
            self.__age = 0

    def get_age(self):
        return self.__age

    def show(self):
        print("%s,%d" % ("person", self.__age))

    # 同理，私有方法
    def __privatefun(self):
        pass

person = Person()
print(person.name)
# print(person.__age)  #对象不能调用私有属性，没有打印值
person.show()  # person,18
person.set_age(10)
print(person.get_age())

# 类属性 实例属性
# 实例属性：和某一个对象有关，多个对象之间不共享
# 类属性：属于类对象，并且多个对象之间是共享的
class People(object):
    address = "suzhou"  # 类属性
    __age = 18

    def __init__(self):  # 实例属性
        self.name = "ls"
        self.age = 20

p = People()
print(p.name, p.address)
print(People.address)

# 类属性的作用距离
class Tool(object):
    num = 0

    def __init__(self, name):
        self.name = name
        Tool.num += 1

t1 = Tool("tool1")
t2 = Tool("tool2")
t2 = Tool("tool3")
print(Tool.num)  # 3

# 类方法
class People(object):
    country = "china"

    @classmethod  # 类方法
    def get_country(cls):
        return cls.country

    @staticmethod  # 静态方法  写死的内容，可以放到静态方法中
    def get_name():
        return People.country
# 从类方法和实例方法以及静态方法的定义形式就可以看出来，类方法的第一个参数是类对象cls，那么通过cls引用的必定是类对象的属性和方法；
# 实例方法的第一个参数是实例对象self，那么通过self引用的可能是类属性、也有可能是实例属性（这个需要具体分析），不过在存在相同名称的类属性和实例属性的情况下，实例属性优先级更高。
# 静态方法中不需要额外定义参数，因此在静态方法中引用类属性的话，必须通过类实例对象来引用

# 多态
# 不同的子类对象调用 相同的父类方法，产生不通的执行结果，可以增加代码的外部 调用灵活度
# 多态以 继承 和重写父类方法 为前提
# 多态是调用方法的技巧，不会影响到类的内部设计
class Animal(object):
    def run(self):
        print('Animal is running……')

class Dog(Animal):
    def run(self):
        print('Dog is running……')

class Cat(Animal):
    def run(self):
        print('Cat is running……')

# 定义一个方法
def run_twice(animal):
    animal.run()

cat = Cat()
dog = Dog()
run_twice(cat)
run_twice(dog)

g_num = 10

def show():
    print('show')

def show1():
    print('show')

class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_inro(self):
        print(self.name, self.age)

print(__name__, "=======")  # First_Module =======
if __name__ == '__main__':
    show()

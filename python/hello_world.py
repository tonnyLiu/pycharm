class Person():
    def __init__(self):
        print("这是构造函数")
    #公有成员
    name = None
    #私有成员
    __age = 24
    def eat(self):
        print("我需要吃饭")

class Student(Person):
    def __init__(self):
        super().__init__()
        print("我也有一个构造函数")

liu = Student()
liu.name = "刘帅"
liu.eat()
print("Hello World OOP!!!")

# 包含一个学生类
# 一个sayHello函数
# 一个打印语句
class Student():
    def __init__(self, name="NoName", age=18):
        self.name = "周震南"
        self.age = 18

    def say(self):
        print("My name is {0}".format(self.name))

def sayHello():
    print("hi, 欢迎来到创造营2019")

print("我是模块p01呀，你叫我干嘛")

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

# 如果只是想要单独执行当前代码时才出现下面这句话，而在调用模块p01时不出现，则使用下面的if判断语句
# 此判断语句建议一直作为程序的入口
# 程序的入口是指程序被执行的第一句话
if __name__ == "__main__":
    print("我是模块p01呀，你叫我干嘛")

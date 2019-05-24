class Student():
    def __init__(self, name="NoName", age=18):
        self.name = "周震南"
        self.age = 18

    def say(self):
        print("My name is {0}".format(self.name))

def sayHello():
    print("hi, 欢迎来到创造营2019")
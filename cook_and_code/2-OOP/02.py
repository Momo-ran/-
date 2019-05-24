class Person():
    name = "朱一龙"
    age = 32
    _petname = "拢龙"  # 小名是受保护的，前面一个下划线，类或者子类可以访问，外部不可以访问
    __score = "sec"  # 考试成绩保密，前面两个下划线表示私有的

    def sleep(self):
        print("sleeping ......")


# 父类写在括号内
class Teacher(Person):
    # 子类中可以定义独有的成员属性和方法
    teacher_id = "9527"

    def make_test(self):
        print("attention")


t = Teacher()
print(t.name)
# 受保护的外部不可以访问，会报错，但是此处为什么可以访问？？？
print(t._petname)
# 私有成员也不可以访问，会报错
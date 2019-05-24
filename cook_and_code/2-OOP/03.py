class Person():
    # 函数的名称可以任意
    def fget(self):
        return self._name * 2
    def fset(self, name):
        # 所有姓名以大写方式保存
        self._name = name.upper()
    def fdel(self):
        self._name = "NoName"
    name = property(fget, fset, fdel, "对name进行操作")
p1 = Person()
p1.name = "zhuyilong"
print(p1.name)
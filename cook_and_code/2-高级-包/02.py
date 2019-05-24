# 先借助于importlib包导入以数字开头的模块名称
import importlib
# 相当于导入一个叫01的模块并把导入模块赋值给了zhuangzaoyin
chuangzaoying = importlib.import_module("01")
# 下面使用的时候就直接用chuangzaoying了
stu = chuangzaoying.Student()
stu.say()

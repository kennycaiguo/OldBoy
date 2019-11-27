#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/26 17:42
# @Author  : Sand
# @FileName: new方法.py
# @Project : OldBoy


# class Student(object):
#     def __init__(self, name):
#         self.name = name
#         print('init hahah')
#
#     def __new__(cls, *args, **kwargs):
#         # 负责执行__init__,进行一些实例初始化之前的工作
#         print(cls, args, kwargs)
#         return object.__new__(cls)
#
#
# p = Student("Alex")
# p.name

# 设计  模式 23设计模式 gof 单例模式

class Printer(object):
    tasks = []
    instance = None

    def __init__(self, name):
        self.name = name

    def add_task(self, job):
        self.tasks.append(job)
        print("[%s]添加任务[%s]到打印机，总任务数[%s]" % (self.name, job, len(self.tasks)))

    def __new__(cls, *args, **kwargs):
        # 只有第一次实例化的时候，正常进行，后面每次实例化，并不是真正的创建一个新实例
        if cls.instance is None:
            # 进行正常的实例化，并把实例化后的对象存在cls.instance里
            obj = object.__new__(cls) # 实例化过程
            print("obj", obj)
            cls.instance = obj  # 把实例化好的对象存下来
        return cls.instance  # 以后的每次实例化，直接返回第一次存的实例对象


p1 = Printer("Word APP")
p2 = Printer("pdf APP")
p3 = Printer("excel APP")

p1.add_task("word file")
p2.add_task("pdffile")
p3.add_task("excel file")

print(p1, p2, p3)
print(p1.name, p2.name, p3.name)

#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/13 9:17
# @Author  : Sand
# @FileName: 依赖关系.py
# @Project : OldBoy
"""
依赖关系：
狗和主人的关系可以理解为是一种依赖关系，如果没有主人，它就是流浪狗了，可能会死。
"""


class Dog:
    def __init__(self, name, age, breed, master):
        self.name = name
        self.age = age
        self.breed = breed
        self.master = master  # master传进来的应该是个对象
        self.sayhi()  # 调用自己的方法在实例化的时候

    def sayhi(self):
        print("Hi, I'm %s, a %s dog, my master is %s" % (self.name, self.breed, self.master.name))


class Person:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def walk_dog(self, dog_obj):
        """遛狗"""
        print("主人[%s]带狗[%s]去溜溜。。。" % (self.name, dog_obj.name))


p = Person("Alex", 26, "Male")
d = Dog("Mjj", 5, "二哈", p)
p.walk_dog(d)

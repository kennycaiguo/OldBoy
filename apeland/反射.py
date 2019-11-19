#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/19 15:05
# @Author  : Sand
# @FileName: 反射.py
# @Project : OldBoy


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        print(self.name, "walking...")


def talk(self):
    print(self.name, "is speaking...")


p = Person("Alex", 22)
if hasattr(p, "name"):
    print("l.....")

# 反射、映射、自省
# getattr()
a = getattr(p, "age")
print(a)

# hasattr()
user_command = input(">>:").strip()
if hasattr(p, user_command):
    func = getattr(p, user_command)
    func()

# setattr()
## static
setattr(p, "sex", "Female")
print(p.sex)
## 方法
setattr(p, "speak", talk)
p.speak(p)

setattr(Person, "speak2", talk)
p.speak2()

# delattr()
delattr(p,"age")
p.age
#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/27 15:22
# @Author  : Sand
# @FileName: TYPE创建类.py
# @Project : OldBoy


class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age


p = Person("Alex", 22)
print(type(p))


def __init__(self, name, age):
    self.name = name
    self.age = age


dog_class = type("Dog", (object,), {"role": "dog", "__init__": __init__})

print(dog_class)

d = dog_class("mjj", 5)
print(d.role, d.name, d.age)
print(dog_class)

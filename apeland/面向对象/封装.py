#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/13 14:09
# @Author  : Sand
# @FileName: 封装.py
# @Project : OldBoy


class Person(object):

    def __init__(self, name, age):
        self.name = name  # 实例变量，成员变量
        self.age = age
        self.__life_val = 100  # 私有变量，私有属性

    def get_life_val(self):
        print("生命值还有", self.__life_val)
        return self.__life_val

    def __breath(self):
        print("%s si breathing..." % (self.name,))

    def got_attack(self):
        self.__life_val -= 20
        print("被攻击了，生命值减20")
        self.__breath()
        return self.__life_val


a = Person("Alex", 20)
# print(a.__life_val)
a.get_life_val()
a.got_attack()
# a.__breath()

# 实例名._类名+方法名()
a._Person__breath()

a._Person__life_val = 10  # 修改私有属性

a.get_life_val()

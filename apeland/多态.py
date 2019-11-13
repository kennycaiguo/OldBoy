#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/13 15:41
# @Author  : Sand
# @FileName: 多态.py
# @Project : OldBoy


class Dog(object):
    def sound(self):
        print("汪汪汪。。。")


class Cat(object):
    def sound(self):
        print("喵喵喵。。。")


def make_sound(animal_obj):
    """统一调用接口"""
    animal_obj.sound()  # 不管你传什么动物进来，我都调用sound()方法


d = Dog()
c = Cat()
make_sound(d)
make_sound(c)

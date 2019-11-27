#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/19 12:43
# @Author  : Sand
# @FileName: property.py
# @Project : OldBoy


class Student(object):

    def __init__(self, name):
        self.name = name

    @property
    def fly(self):
        print(self.name, "is flying....")


s = Student("Jack")
s.fly

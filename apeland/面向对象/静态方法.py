#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/18 18:19
# @Author  : Sand
# @FileName: 静态方法.py
# @Project : OldBoy


class Student(object):
    role = "Stu"

    def __init__(self, name):
        self.name = name

    @staticmethod
    def fly(self):
        print(self.name, "is flying...")

    @staticmethod
    def walk():
        print("Student is walking...")


s = Student("Jack")
s.fly(s)
s.walk()

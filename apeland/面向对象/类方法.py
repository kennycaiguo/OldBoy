#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/18 17:31
# @Author  : Sand
# @FileName: 类方法.py
# @Project : OldBoy


class Student(object):
    __stu_num = 0

    def __init__(self, name):
        self.name = name
        # Student.stu_num += 1
        self.add_num(self)
        print("生成一个学生：", self.name, self.__stu_num)

    @classmethod
    def add_num(cls, obj):
        if obj.name:
            cls.__stu_num += 1


s1 = Student('Alex')
s2 = Student('Mars')
s3 = Student('Tony')
# print(Student.__stu_num + 1)

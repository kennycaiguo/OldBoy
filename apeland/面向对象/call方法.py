#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/27 10:58
# @Author  : Sand
# @FileName: call方法.py
# @Project : OldBoy


class School:
    def __init__(self, name, addr, type):
        self.name = name
        self.addr = addr
        self.type = type

    def __call__(self, *args, **kwargs):
        print(self, args, kwargs)


s = School("apeland", "beijing", "master")
s() # 实例名() 就执行

# School()()
#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/26 17:37
# @Author  : Sand
# @FileName: del析构.py
# @Project : OldBoy


class School:
    def __init__(self, name, addr, tpype):
        self.name = name
        self.addr = addr
        self.type = type

    def __del__(self):
        print("对象被释放了。。。")


s = School("apeland", "beijing", "master")
print("ddd")
print("ddd")
print("ddd")
del s
print("ddd")
print("ddd")

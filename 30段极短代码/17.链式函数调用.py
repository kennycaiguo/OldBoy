#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/12 10:44
# @Author  : Sand
# @FileName: 17.链式函数调用.py
# @Project : OldBoy


"""
你可以在一行代码内调用多个函数。
"""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


a, b = 4, 5
print((subtract if a > b else add)(a, b))  # 9

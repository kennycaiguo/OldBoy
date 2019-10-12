#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/12 15:55
# @Author  : Sand
# @FileName: 23.Try else.py
# @Project : OldBoy


"""
我们在使用 try/except 语句的时候也可以加一个 else 子句，如果没有触发错误的话，这个子句就会被运行
"""


try:
    2*3
except TypeError:
    print("An exception was raised")
else:
    print("Thank God, no exceptions were raised.")

# Thank God, no exceptions were raised.

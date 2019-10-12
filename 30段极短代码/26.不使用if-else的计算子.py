#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/12 16:00
# @Author  : Sand
# @FileName: 26.不使用if-else的计算子.py
# @Project : OldBoy


"""
这一段代码可以不使用条件语句就实现加减乘除、求幂操作，它通过字典这一数据结构实现
"""

import operator

action = {
    "+": operator.add,
    "-": operator.sub,
    "/": operator.truediv,
    "*": operator.mul,
    "**": pow
}
print(action['-'](50, 25))  # 25

#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/12 10:41
# @Author  : Sand
# @FileName: 16.通过函数取差.py
# @Project : OldBoy


"""
如下方法首先会应用一个给定的函数，然后再返回应用函数后结果有差别的列表元素。
"""

from math import floor


def difference_by(a, b, fn):
    b = set(map(fn, b))
    return [item for item in a if fn(item) not in b]


difference_by([2.1, 1.2], [2.3, 3.4], floor)  # [1.2]
difference_by([{'x': 2}, {'x': 1}], [{'x': 1}], lambda v: v['x'])
# [ { x: 2 } ]

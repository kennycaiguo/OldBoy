#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/12 10:46
# @Author  : Sand
# @FileName: 18.检查重复项.py
# @Project : OldBoy


"""
如下代码将检查两个列表是不是有重复项
"""


def has_duplicates(lst):
    return len(lst) != len(set(lst))


x = [1, 2, 3, 4, 5, 5]
y = [1, 2, 3, 4, 5]
has_duplicates(x)  # True
has_duplicates(y)  # False

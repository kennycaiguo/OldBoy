#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/12 10:47
# @Author  : Sand
# @FileName: 19.合并两个字典.py
# @Project : OldBoy


def merge_two_dicts(a, b):
    c = a.copy()  # make a copy of a
    c.update(b)  # modify keys and values of a with the ones from b
    return c


a = {'x': 1, 'y': 2}
b = {'y': 3, 'z': 4}
print(merge_two_dicts(a, b))


# {'y': 3, 'x': 1, 'z': 4}


def merge_dictionaries(a, b):
    return {**a, **b}


# 在 Python 3.5 或更高版本中，我们也可以用以下方式合并字典：

a = {'x': 1, 'y': 2}
b = {'y': 3, 'z': 4}
print(merge_dictionaries(a, b))
# {'y': 3, 'x': 1, 'z': 4}

#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/12 10:49
# @Author  : Sand
# @FileName: 20.将两个列表转化为字典.py
# @Project : OldBoy


def to_dictionary(keys, values):
    return dict(zip(keys, values))


keys = ["a", "b", "c"]
values = [2, 3, 4]
print(to_dictionary(keys, values))
# {'a': 2, 'c': 4, 'b': 3}

#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/12 16:03
# @Author  : Sand
# @FileName: 28.展开列表.py
# @Project : OldBoy


"""
将列表内的所有元素，包括子列表，都展开成一个列表。
"""


def spread(arg):
    ret = []
    for i in arg:
        if isinstance(i, list):
            ret.extend(i)
        else:
            ret.append(i)
    return ret


spread([1, 2, 3, [4, 5, 6], [7], 8, 9])  # [1,2,3,4,5,6,7,8,9]

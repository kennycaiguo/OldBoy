#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/12 10:39
# @Author  : Sand
# @FileName: 14.展开列表.py
# @Project : OldBoy


"""
该方法将通过递归的方式将列表的嵌套展开为单个列表
"""


def spread(arg):
    ret = []
    for i in arg:
        if isinstance(i, list):
            ret.extend(i)
        else:
            ret.append(i)
    return ret


def deep_flatten(lst):
    result = []
    result.extend(
        spread(list(map(lambda x: deep_flatten(x) if type(x) == list else x, lst))))
    return result


deep_flatten([1, [2], [[3], 4], 5])  # [1,2,3,4,5]

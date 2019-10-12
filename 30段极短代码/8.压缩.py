#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/12 10:33
# @Author  : Sand
# @FileName: 8.压缩.py
# @Project : OldBoy


"""
这个方法可以将布尔型的值去掉，例如（False，None，0，“”），它使用 filter() 函数。
"""

def compact(lst):
    return list(filter(bool, lst))


compact([0, 1, False, 2, '', 3, 'a', 's', 34])
# [ 1, 2, 3, 'a', 's', 34 ]
#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/12 15:56
# @Author  : Sand
# @FileName: 24.元素频率.py
# @Project : OldBoy


"""
下面的方法会根据元素频率取列表中最常见的元素。
"""


def most_frequent(lst):
    return max(set(lst), key=list.count)


lst = [1, 2, 1, 2, 3, 2, 1, 4, 2]
most_frequent(lst)

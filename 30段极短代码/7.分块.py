#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/12 10:30
# @Author  : Sand
# @FileName: 7.分块.py
# @Project : OldBoy


from math import ceil
'''
给定具体的大小，定义一个函数以按照这个大小切割列表。
'''


def chunk(lst, size):
    return list(
        map(lambda x: lst[x * size:x * size + size],
            list(range(0, ceil(len(lst) / size)))))


chunk([1, 2, 3, 4, 5], 2)
# [[1,2],[3,4],5]

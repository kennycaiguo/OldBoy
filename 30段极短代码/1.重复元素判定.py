#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/11 17:33
# @Author  : Sand
# @FileName: 1.重复元素判定.py
# @Project : OldBoy


def all_unique(lst):
    return len(lst) == len(set(lst))


x = [1, 1, 2, 2, 3, 2, 3, 4, 5, 6]
print(len(set(x)))
y = [1, 2, 3, 4, 5]
print(all_unique(x))
print(all_unique(y))

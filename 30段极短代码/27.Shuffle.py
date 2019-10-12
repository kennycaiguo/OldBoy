#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/12 16:02
# @Author  : Sand
# @FileName: 27.Shuffle.py
# @Project : OldBoy


"""
该算法会打乱列表元素的顺序，它主要会通过 Fisher-Yates 算法对新列表进行排序
"""

from copy import deepcopy
from random import randint


def shuffle(lst):
    temp_lst = deepcopy(lst)
    m = len(temp_lst)
    while (m):
        m -= 1
        i = randint(0, m)
        temp_lst[m], temp_lst[i] = temp_lst[i], temp_lst[m]
    return temp_lst


foo = [1, 2, 3]
shuffle(foo)  # [2,3,1] , foo = [1,2,3]

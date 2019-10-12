#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/12 16:06
# @Author  : Sand
# @FileName: 29.交换值.py
# @Project : OldBoy


"""
不需要额外的操作就能交换两个变量的值
"""

def spread(arg):
    ret = []
    for i in arg:
        if isinstance(i, list):
            ret.extend(i)
        else:
            ret.append(i)
    return ret

def swap(a, b):
  return b, a

a, b = -1, 14
swap(a, b) # (14, -1)
spread([1,2,3,[4,5,6],[7],8,9]) # [1,2,3,4,5,6,7,8,9]
#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/12 10:34
# @Author  : Sand
# @FileName: 9.解包.py
# @Project : OldBoy


"""
如下代码段可以将打包好的成对列表解开成两组不同的元组。
"""


array = [['a', 'b'], ['c', 'd'], ['e', 'f']]
transposed = zip(*array)
print(transposed)
# [('a', 'c', 'e'), ('b', 'd', 'f')]
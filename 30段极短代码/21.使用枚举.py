#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/12 10:50
# @Author  : Sand
# @FileName: 21.使用枚举.py
# @Project : OldBoy


"""
我们常用 For 循环来遍历某个列表，同样我们也能枚举列表的索引与值
"""

list = ["a", "b", "c", "d"]
for index, element in enumerate(list):
    print("Value", element, "Index ", index, )

# ('Value', 'a', 'Index ', 0)
# ('Value', 'b', 'Index ', 1)
# ('Value', 'c', 'Index ', 2)
# ('Value', 'd', 'Index ', 3)

#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/12 16:08
# @Author  : Sand
# @FileName: 30.字典默认值.py
# @Project : OldBoy


"""
通过 Key 取对应的 Value 值，可以通过以下方式设置默认值。如果 get() 方法没有设置默认值，那么如果遇到不存在的 Key，则会返回 None。
"""

d = {'a': 1, 'b': 2}

print(d.get('c', 3)) # 3
#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/12 10:38
# @Author  : Sand
# @FileName: 13.首字母小写.py
# @Project : OldBoy


"""
如下方法将令给定字符串的第一个字符统一为小写。
"""


def decapitalize(string):
    return str[:1].lower() + str[1:]


decapitalize('FooBar') # 'fooBar'
decapitalize('FooBar') # 'fooBar'

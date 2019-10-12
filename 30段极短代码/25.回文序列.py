#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/12 15:58
# @Author  : Sand
# @FileName: 25.回文序列.py
# @Project : OldBoy


"""
以下方法会检查给定的字符串是不是回文序列，它首先会把所有字母转化为小写，并移除非英文字母符号。最后，它会对比字符串与反向字符串是否相等，相等则表示为回文序列
"""


def palindrome(string):
    from re import sub
    s = sub('[\W_]', '', string.lower())
    return s == s[::-1]


palindrome('taco cat')  # True

#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/12 10:37
# @Author  : Sand
# @FileName: 12.元音统计.py
# @Project : OldBoy


"""
以下方法将统计字符串中的元音 (‘a’,‘e’,‘i’,‘o’,‘u’) 的个数，它是通过正则表达式做的。
"""

import re


def count_vowels(str):
    return len(len(re.findall(r'[aeiou]', str, re.IGNORECASE)))


count_vowels('foobar')  # 3
count_vowels('gym')  # 0

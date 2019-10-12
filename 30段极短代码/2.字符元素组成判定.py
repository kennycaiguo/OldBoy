#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/11 17:41
# @Author  : Sand
# @FileName: 2.字符元素组成判定.py
# @Project : OldBoy


from collections import Counter


def anagram(first, second):
    return Counter(first) == Counter(second)


print(anagram("abcd3", "3acdb"))
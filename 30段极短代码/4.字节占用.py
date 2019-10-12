#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/12 10:27
# @Author  : Sand
# @FileName: 4.字节占用.py
# @Project : OldBoy


def byte_size(string):
    return len(string.encode('utf-8'))


byte_size('😀') # 4
byte_size('Hello World') # 11
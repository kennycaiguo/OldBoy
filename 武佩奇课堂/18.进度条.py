#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/6/28 17:47
# @Author  : Sand
# @FileName: 17.斐波拉契数列.py
# @Project : OldBoy


import sys
import time

for i in range(1, 101):
    msg = '\r%s%%' % i
    print(msg, end='')
    time.sleep(0.2)

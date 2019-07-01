#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/6/28 17:47
# @Author  : Sand
# @FileName: 17.斐波拉契数列.py
# @Project : OldBoy

import time


def func(max_range):
    result = []
    while True:
        if len(result) == 0:
            result.append(1)
        elif len(result) == 1:
            result.append(1)
        else:
            val = result[-1] + result[-2]
            if val > max_range:
                break
            result.append(val)
        # print(result)
        # time.sleep(1)
    return result


s = func(100)
print(s)

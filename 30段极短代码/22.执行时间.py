#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/12 15:54
# @Author  : Sand
# @FileName: 22.执行时间.py
# @Project : OldBoy


"""
如下代码块可以用来计算执行特定代码所花费的时间
"""


import time

start_time = time.time()

a = 1
b = 2
c = a + b
print(c) #3

end_time = time.time()
total_time = end_time - start_time
print("Time: ", total_time)

# ('Time: ', 1.1205673217773438e-05)

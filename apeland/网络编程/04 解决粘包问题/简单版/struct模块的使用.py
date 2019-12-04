#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/12/4 16:43
# @Author  : Sand
# @FileName: struct模块的使用.py
# @Project : OldBoy
import struct


res = struct.pack('i', 1230)
print(res, type(res), len(res))

# client.recv(4)
obj = struct.unpack('i', res)
print(obj)

res1 = struct.pack('l', 43275934759435932459073097)
print(res1, len(res1))

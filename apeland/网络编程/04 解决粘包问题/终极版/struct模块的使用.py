#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/12/4 16:43
# @Author  : Sand
# @FileName: struct模块的使用.py
# @Project : OldBoy
import struct
import json

# res = struct.pack('i', 1230)
# print(res, type(res), len(res))
#
# # client.recv(4)
# obj = struct.unpack('i', res)
# print(obj)
#
# res1 = struct.pack('l', 43275934759435932459073097)
# print(res1, len(res1))

header_dic = {
    'filename': 'a.txt',
    'md5': 'fsdafjsalj',
    'total_size': '35429579123759237'
}

header_json = json.dumps(header_dic)
print(header_json, type(header_json))
header_bytes = header_json.encode('gbk')
print(header_bytes, type(header_bytes))

struct.pack('i', len(header_bytes))
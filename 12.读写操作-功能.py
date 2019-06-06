#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/6/6 17:23
# @Author  : Sand
# @FileName: 12.读写操作-功能.py
# @Project : OldBoy

############# 读操作 #########################################
"""
# file_object = open('log.txt', mode='r', encoding='utf-8')

# 读取文件的所有内容到内存
# data = file_object.read()

# 从当前光标所在的位置向后读取文件的2个字符
# data = file_object.read(2)
# print(data)

# 读取文件的所有内容到内存,并按照每一行进行分割到列表中
# data = file_object.readlines()
# print(data)

# 如果以后读取一个特别大的文件  (***********用的最多*************)
# for line in file_object:
#     line = line.strip()
#     print(line)

# file_object.close()
"""

############# 写操作 #########################################
file_object = open('log.txt', mode='w', encoding='utf-8')

file_object.write('你好\n')
file_object.write('小黑')


file_object.close()
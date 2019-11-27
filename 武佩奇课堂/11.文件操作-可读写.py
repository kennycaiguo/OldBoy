#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/6/6 16:55
# @Author  : Sand
# @FileName: 11.文件操作-可读写.py
# @Project : OldBoy


# 可读可写
"""

读取
写入：根据光标的位置，从当前光标位置开始进行写入操作（可能会将其他的蚊子覆盖）

file_object = open('log.txt', mode='r+',encoding='utf-8') # r,read(只读);w,write(只写，先清空，一般用于新建文件);a,append
# file_object.seek(3)   # 调整光标的位置

# 读取内容
content = file_object.read()
file_object.write('狼')

# 关闭文件
file_object.close()
"""


# 可读可写
# 写入时会将文件清空，读取时需要调整光标
"""
file_object = open('log.txt', mode='w+',encoding='utf-8') # r,read(只读);w,write(只写，先清空，一般用于新建文件);a,append
data = file_object.read()
print(data)
file_object.write('alex')
file_object.seek(0)
data = file_object.read()
print(data)
file_object.close()
"""

# 可读可写
file_object = open('log.txt', mode='a+',encoding='utf-8') # r,read(只读);w,write(只写，先清空，一般用于新建文件);a,append
# file_object.seek(0)
# data = file_object.read()
# print(data)

file_object.seek(0)
file_object.write('666')

file_object.close()
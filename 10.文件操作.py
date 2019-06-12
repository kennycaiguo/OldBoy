#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/6/6 16:29
# @Author  : Sand
# @FileName: 10.文件操作.py
# @Project : OldBoy



################### 读取示例:r，只读不能写，+ 文件不存在报错 ############################
'''
# 打开文件
file_object = open('log.txt', mode='r',encoding='utf-8') # r,read;w,write;a,append

# 读取文件
content = file_object.read()
print(content)

# 关闭文件
file_object.close()
'''

################### 写入示例:w，只写不能读（先清空文件）+ 文件不存在新建###################
'''
# 打开文件
file_object = open('log.txt', mode='w',encoding='utf-8') # r,read(只读);w,write(只写，先清空，一般用于新建文件);a,append

# 写内容
content = file_object.write('李忠伟')

# 关闭文件
file_object.close()
'''

################### 追加示例:a，只追加不能读 + 文件不存在则新建 ##########################
'''
# 打开文件
file_object = open('log.txt', mode='a',encoding='utf-8') # r,read(只读);w,write(只写，先清空，一般用于新建文件);a,append

# 写内容
content = file_object.write('你好')

# 关闭文件
file_object.close()
'''

f = open('a.txt', mode='wb')
# 1. 把要写入的字符串转换成二进制
data = '我好困'
content = data.encode('utf-8')

# 2. 再将二进制写到文件中
f.write(content)  # wb打开文件，则write传入的是二进制
f.close()

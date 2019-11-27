#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/6/28 15:28
# @Author  : Sand
# @FileName: 16.练习题.py
# @Project : OldBoy

# 3. 读取文件，将文件的内容构造成指定格式的数据，并返回。
"""
a.log文件
    alex|123|18
    eric|uiuf|19
    ...
目标结构：
a.  ["alex|123|18","eric|uiuf|19"] 并返回。
b. [['alex','123','18'],['eric','uiuf','19']]
c. [
	{'name':'alex','pwd':'123','age':'18'},
	{'name':'eric','pwd':'uiuf','age':'19'},
]
"""


def write_file_to_list(file):
    new_list = []
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            s = line.strip()
            new_list.append(s)
    return new_list


def write_file_to_list1(file):
    new_list = []
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            l = line.strip().split('|')
            new_list.append(l)
    return new_list


def write_file_to_dict(file):
    new_list = []
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            dict = {}
            l = line.strip().split('|')
            dict['name'] = l[0]
            dict['pwd'] = l[1]
            dict['age'] = l[2]
            new_list.append(dict)
    return new_list


li = write_file_to_list('a.log')
print(li)

li = write_file_to_list1('a.log')
print(li)

li = write_file_to_dict('a.log')
print(li)

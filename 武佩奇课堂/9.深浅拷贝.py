#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/6/6 15:34
# @Author  : Sand
# @FileName: 9.深浅拷贝.py
# @Project : OldBoy

'''

- 浅拷贝：拷贝第一层
- 深拷贝：拷贝所有数据（可变）

'''
'''
#  应该每次拷贝一份（但由于属于小数据）
v1 = 'alex'
import copy
v2 = copy.copy(v1)
print(id(v1), id(v2))

v3 = copy.deepcopy(v1)
print(id(v1), id(v3))
'''
'''
v1 = [1,2,3,4]
import copy
v2 = copy.copy(v1)
print(id(v1), id(v2))

v3 = copy.deepcopy(v1)
print(id(v1), id(v3))
'''

# v1 = [1,2,3,4,[11,22,33]]
import copy
# v2 = copy.copy(v1)
# print(id(v1), id(v2))
# print(id(v1[4]), id(v2[4]))

# v3 = copy.deepcopy(v1)
# print(id(v1), id(v3))
# print(id(v1[4]), id(v3[4]))

# 练习1
v1 = [1,2,3]
v2 = copy.copy(v1)
print(v1 == v2)
print(v1 is v2)
print(v1[0] is v2[0])
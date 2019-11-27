#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/26 11:07
# @Author  : Sand
# @FileName: 双下线方法.py
# @Project : OldBoy


class Brand:
    def __init__(self, name):
        self.name = name

    def __getitem__(self, item):
        print('get item....', self.__dict__[item])

    def __setitem__(self, key, value):
        print('set item')
        self.__dict__[key] = value

    def __delitem__(self, key):
        print('__del...')

    def __delattr__(self, item):
        print('del obj.key时，我执行')
        self.__dict__.pop(item)


b = Brand("小猿圈")
b['name']
b['website'] = "www.apeland.cn"
print(b.website)

del b['name']

del b.name

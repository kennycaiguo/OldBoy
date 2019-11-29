#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/28 11:39
# @Author  : Sand
# @FileName: 异常处理.py
# @Project : OldBoy


class MyException(BaseException):
    def __init__(self, msg):
        self.message = msg

    def __str__(self):
        return self.message


try:
    raise MyException("我的错误")
except MyException as e:
    print(e)
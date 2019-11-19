#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/19 17:09
# @Author  : Sand
# @FileName: 反射登录应用.py
# @Project : OldBoy


class User(object):
    def login(self):
        print("欢迎来到登录页面")

    def register(self):
        print("欢迎来到注册页面")

    def save(self):
        print("欢迎来到存储页面")


user = User()
while 1:
    choose = input('>>>').strip()
    if hasattr(user, choose):
        func = getattr(user, choose)
        func()
    else:
        print("输入错误...")
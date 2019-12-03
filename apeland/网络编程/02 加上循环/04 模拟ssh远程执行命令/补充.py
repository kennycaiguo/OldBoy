#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/12/3 17:10
# @Author  : Sand
# @FileName: 补充.py
# @Project : OldBoy

"""
windows:
1. dir: 查看某个文件夹下的子文件名与子文件夹名
2. ipconfig: 查看本低网卡的ip信息
3. tasklist: 查看运行的进程

linux:
1. ls
2. ifconfig
3. ps -aux
"""

# 执行系统命令，并且拿到命令的结果
# import os
# res = os.system('dir .')
# print('命令的结果是：', res)

import subprocess

obj = subprocess.Popen('dir .', shell=True,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)

print(obj)
print('stdout 1--->:', obj.stdout.read().decode('gbk'))  # linux是utf-8编码，windows是gbk编码
print('stderr 1--->:', obj.stderr.read().decode('gbk'))

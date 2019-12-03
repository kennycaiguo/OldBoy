#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/12/2 17:47
# @Author  : Sand
# @FileName: 客户端.py
# @Project : OldBoy
import socket

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(phone)
phone.connect(('127.0.0.1', 8081))

while True:
    # 1、 发命令
    cmd = input('>>>: ').strip()
    if not cmd: continue
    phone.send(cmd.encode('utf-8'))

    # 2、拿命令的结果，并打印
    data = phone.recv(1024)  # 1024是一个坑
    print(data.decode('gbk'))

phone.close()

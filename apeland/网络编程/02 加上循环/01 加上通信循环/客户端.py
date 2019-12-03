#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/12/2 17:47
# @Author  : Sand
# @FileName: 客户端.py
# @Project : OldBoy


import socket

# 1、买手机
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(phone)

# 2、 拨号
phone.connect(('127.0.0.1', 8081))

# 3、 发、收消息
while True:
    msg = input('>>>: ').strip()
    phone.send(msg.encode('utf-8'))
    data = phone.recv(1024)
    print('服务端的数据', data)

# 4、 关机
phone.close()

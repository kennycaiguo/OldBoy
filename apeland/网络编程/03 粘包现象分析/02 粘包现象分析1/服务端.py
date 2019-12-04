#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/12/4 14:07
# @Author  : Sand
# @FileName: 服务端.py
# @Project : OldBoy
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 8081))  # 0-65535: 0-1024给操作系统使用
server.listen(5)

print('starting...')
conn, addr = server.accept()

res1 = conn.recv(1024)
print('第一次', res1)

res2 = conn.recv(1024)
print('第二次', res2)

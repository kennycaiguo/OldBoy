#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/12/2 17:47
# @Author  : Sand
# @FileName: 服务端.py
# @Project : OldBoy
import socket

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
phone.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
phone.bind(('127.0.0.1', 8081))  # 0-65535: 0-1024给操作系统使用
phone.listen(5)

print('starting...')
conn, client_addr = phone.accept()
print(client_addr)

while True:  # 通信循环
    try:
        data = conn.recv(1024)  # 1、 单位：bytes 2、1024代表最大接收1024个bytes
        if not data: break   # 适用于Linux操作系统
        print("客户端的数据", data)
        conn.send(data.upper())
    except ConnectionResetError:   # 适用于Windows操作系统
        break

conn.close()
phone.close()

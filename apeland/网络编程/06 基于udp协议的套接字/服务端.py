#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/12/5 15:24
# @Author  : Sand
# @FileName: 服务端.py
# @Project : OldBoy
from socket import *

server = socket(AF_INET, SOCK_DGRAM)
server.bind(('127.0.0.1', 8080))

# server.listen(5)
# while True:
#     conn,addr = server.accept()

while True:
    data, client_addr = server.recvfrom(1024)
    print(data)

    server.sendto(data.upper(), client_addr)

server.close()

#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/12/5 15:23
# @Author  : Sand
# @FileName: 客户端.py
# @Project : OldBoy
from socket import *

client = socket(AF_INET, SOCK_DGRAM)

while True:
    msg = input('>>:').strip()
    client.sendto(msg.encode('gbk'), ('127.0.0.1', 8080))

    data, server_addr = client.recvfrom(1024)
    print(data, server_addr)

client.close()
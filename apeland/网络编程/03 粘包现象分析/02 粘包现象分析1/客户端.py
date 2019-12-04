#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/12/4 14:08
# @Author  : Sand
# @FileName: 客户端.py
# @Project : OldBoy
import socket
import time

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8081))

client.send('hello'.encode())
time.sleep(5)
client.send('world'.encode())


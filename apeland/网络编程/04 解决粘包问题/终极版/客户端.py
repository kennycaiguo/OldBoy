#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/12/2 17:47
# @Author  : Sand
# @FileName: 客户端.py
# @Project : OldBoy
import socket
import struct
import json

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(phone)
phone.connect(('127.0.0.1', 8081))

while True:
    # 1、 发命令
    cmd = input('>>>: ').strip()
    if not cmd: continue
    phone.send(cmd.encode('gbk'))

    # 2、拿命令的结果，并打印

    # 第一步： 先收报头的长度
    obj = phone.recv(4)
    header_size = struct.unpack('i', obj)[0]

    # 第二步：再收报头
    header_bytes = phone.recv(header_size)

    # 第三步：从报头中解析出对真实数据的描述信息（数据的长度）
    header_json = header_bytes.decode('gbk')
    header_dic = json.loads(header_json)
    print('报头信息：', header_dic)
    total_size = header_dic['total_size']

    # 第四步：接收真实的数据
    recv_size = 0
    recv_data = b''
    while recv_size < total_size:
        res = phone.recv(1024)
        recv_data += res
        recv_size += len(res)
    print(recv_data.decode('gbk'))
phone.close()

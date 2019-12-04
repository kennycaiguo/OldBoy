#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/12/2 17:47
# @Author  : Sand
# @FileName: 服务端.py
# @Project : OldBoy
import socket
import subprocess
import struct

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
phone.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
phone.bind(('127.0.0.1', 8081))  # 0-65535: 0-1024给操作系统使用
phone.listen(5)

print('starting...')
while True:  # 链接循环
    conn, client_addr = phone.accept()
    print(client_addr)

    while True:  # 通信循环
        try:
            # 1、 收命令
            cmd = conn.recv(1024)  # 1、 单位：bytes 2、1024代表最大接收1024个bytes
            if not cmd: break
            print("客户端的数据", cmd)

            # 2、 执行命令，拿到结果
            obj = subprocess.Popen(cmd.decode('gbk'), shell=True,  # linux是utf-8编码，windows是gbk编码
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
            stdout = obj.stdout.read()
            stderr = obj.stderr.read()

            # 3、 把命令的结果返回给客户端
            # 第一步： 制作固定长度的包头
            total_size = len(stdout) + len(stderr)
            header = struct.pack('i', total_size)

            # 第二步：把报头（固定长度）发送给客户端
            conn.send(header)

            # 第三步： 再发送真是的数据
            conn.send(stdout)
            conn.send(stderr)
        except ConnectionResetError:  # 使用户Windows操作系统
            break
    conn.close()
phone.close()

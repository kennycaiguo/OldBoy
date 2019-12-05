#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/12/2 17:47
# @Author  : Sand
# @FileName: 服务端.py
# @Project : OldBoy
import socket
import struct
import json
import os

share_dir = r'C:\Users\Administrator\PycharmProjects\OldBoy\apeland\网络编程\05_文件传输\简单版\server\share'

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
            res = conn.recv(1024)  # b'get a.txt'
            if not res: break
            print("客户端的数据", res)

            # 2、 解析命令，提取相应命令参数
            cmds = res.decode('gbk').split()  # ['get','a.txt']
            filename = cmds[1]

            # 3、 以读的方式打开问价，读取文件内容发送给客户端
            # 第一步： 制作固定长度的包头
            header_dic = {
                'filename': filename,
                'md5': 'fsdafjsalj',
                'file_size': os.path.getsize(r'%s/%s' % (share_dir, filename))
            }

            header_json = json.dumps(header_dic)
            header_bytes = header_json.encode('gbk')

            # 第二步：先发报头的长度
            conn.send(struct.pack('i', len(header_bytes)))

            # 第三步： 再发送报头
            conn.send(header_bytes)

            # 第四步： 再发送真是的数据
            with open('%s/%s' % (share_dir, filename), 'rb') as f:
                # conn.send(f.read())
                for line in f:
                    conn.send(line)
        except ConnectionResetError:  # 使用户Windows操作系统
            break
    conn.close()
phone.close()

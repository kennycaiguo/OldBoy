#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/12/2 17:47
# @Author  : Sand
# @FileName: 客户端.py
# @Project : OldBoy
import socket
import struct
import json
import time

download_dir = r'C:\Users\Administrator\PycharmProjects\OldBoy\apeland\网络编程\05_文件传输\简单版\client\download'

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(phone)
phone.connect(('127.0.0.1', 8081))

while True:
    # 1、 发命令
    cmd = input('>>>: ').strip()  # get a.txt
    if not cmd: continue
    phone.send(cmd.encode('gbk'))

    # 2、以写的方式打开一个新文件，接收服务端发来的文件的内容写入客户的新文件
    # 第一步： 先收报头的长度
    obj = phone.recv(4)
    header_size = struct.unpack('i', obj)[0]

    # 第二步：再收报头
    header_bytes = phone.recv(header_size)

    # 第三步：从报头中解析出对真实数据的描述信息（数据的长度）
    header_json = header_bytes.decode('gbk')
    header_dic = json.loads(header_json)
    print('报头信息：', header_dic)
    total_size = header_dic['file_size']
    filename = header_dic['filename']

    # 第四步：接收真实的数据
    with open('%s/%s' % (download_dir, filename), 'wb') as f:
        recv_size = 0
        while recv_size < total_size:
            line = phone.recv(1024)
            f.write(line)
            recv_size += len(line)
            msg = '\r%s%%' % round(recv_size / total_size * 100, 2)
            print(msg, end='')
            time.sleep(0.002)
            # print('总大小：%s   已下载：%s' %(total_size, recv_size))
phone.close()

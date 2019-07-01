#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/6/14 15:21
# @Author  : Sand
# @FileName: 15.发送邮件.py
# @Project : OldBoy


import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

msg = MIMEText('导演，我想演男一号，你想怎么着都行 。', 'plain', 'utf-8')
msg['From'] = formataddr(['QQ', '29268036@qq.com'])
msg['To'] = formataddr(['工作', 'yinl10@chinaunicom.cn'])
msg['Subject'] = '亲爱的导演'

server = smtplib.SMTP('smtp.qq.com')
server.login('29268036@qq.com', '714yy714717rr717')
server.sendmail('29268036@qq.com', ['yinl10@chinaunicom.cn', ], msg.as_string())
server.quit()

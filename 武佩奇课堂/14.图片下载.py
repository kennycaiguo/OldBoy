#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/6/10 16:34
# @Author  : Sand
# @FileName: 14.图片下载.py
# @Project : OldBoy

import requests

url = 'https://www2.autoimg.cn/newsdfs/g1/M0B/6C/5E/120x90_0_autohomecar__ChsEmVz5v92APRPaAAFYV0oo0UI590.jpg'
r1 = requests.get(url)

f = open('v1.jpg', mode='wb')
f.write(r1.content)
f.close()

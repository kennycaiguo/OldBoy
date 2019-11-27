#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/6/10 15:30
# @Author  : Sand
# @FileName: 13.初始爬虫.py
# @Project : OldBoy

import requests
from bs4 import BeautifulSoup

# 1. python模拟浏览器向 https://www.autohome.com.cn/news/ 发送请求
response = requests.get('https://www.autohome.com.cn/news/')

# 2. 去字符串中找我想要的东西（先将二进制转换成字符串）
# print(response.content)
data = response.content.decode('gb2312')

soup = BeautifulSoup(data, features='html.parser')
container = soup.find(id='auto-channel-lazyload-article')

li_list = container.find_all(name='li')
for item in li_list:
    tag = item.find(name='h3')
    if not tag:
        continue
    img_url = "https:" + item.find(name='img').get('src')
    print(tag.text, img_url)
    print('=' * 50)



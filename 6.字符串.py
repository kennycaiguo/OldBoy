# -*- coding: utf-8 -*-
# @Time    : 2019/5/20 14:40
# @Author  : Sand
# @FileName: 6.字符串.py
# @Project : OldBoy

'''


user = input('请输入用户名：')

new_user1 = user.rstrip()
new_user2 = new_user1.lstrip()

data = new_user2.upper()

print('...>', data, '<---')
'''

# message = input('请说话：')
# print(message)
#
# data = message.replace('大爷', '**', 1)
# print(data)

message = "小黑现在一脸懵逼，因为昨天晚上一直学习，直到深夜。"
# result = message.split("，", 1)
result = message.rsplit("，", 1)

print(result)

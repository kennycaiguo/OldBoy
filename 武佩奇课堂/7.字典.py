# -*- coding: utf-8 -*-
# @Time    : 2019/6/4 14:18
# @Author  : Sand
# @FileName: 7.字典.py
# @Project : OldBoy

'''
# info = {"name" : "刘伟达", "age" : 18, "gender" : "男", "hobby" : "同桌"}
#
# for key in info.keys():
#     print(key)
#
# for key, val in info.items():
#     print(key, val)
#
# for item in info.items():
#     print(item)
'''
# 6. 给你一个空字典，请一直让用户输入：key，value， 将输入的key和value添加到字典中，直到用户输入N，则表示不输入
'''
info = {}
while True:
    k = input("请输入键：")
    if k == 'N':
        break
    v = input("请输入值：")
    info[k] = v
print(info)
'''
# 7.请用代码实现
'''
    message = "k1|v1,k2|v2,k3|123"
    
    info = {'k1':'v1', 'k2':'v2','k3':'v3'}

# message = "k1|v1,k2|v2,k3|123"
# info = {}
# for i in message.split(','):
#     key, val = i.split('|')
#     info[key] = val
# print(info)
'''
# 9. 创建一个用户列表，然后让用户输入用户名和密码进行登录
"""
    user_list = [
        {'user':'用户输入', 'pwd':'用户输入'},
        {'user':'用户输入', 'pwd':'用户输入'},
        {'user':'用户输入', 'pwd':'用户输入'},
        {'user':'用户输入', 'pwd':'用户输入'},   
        {'user':'用户输入', 'pwd':'用户输入'},  # N
    ]

user_list = []
while True:
    user_info = {}
    u = input("请输入用户：")
    if u == "N":
        break
    p = input("请输入密码：")
    user_info['user'] = u.strip()
    user_info['pwd'] = p.strip()
    user_list.append(user_info)
print(user_list)

print("请进行登录".center(50, '-'))

username = input("请输入用户名：").strip()
password = input("请输入密码：").strip()

message = "登录失败"
for item in user_list:
    if username == item['user'] and password == item['pwd']:
        message= '登录成功'
        break
print(message)
"""

# 10. 有序
# 有序：元组/列表
# 无序：字典（py3.6之后字典就是有序了）


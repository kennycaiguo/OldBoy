# -*- coding: utf-8 -*-
# @Time    : 2019/5/13 14:50
# @Author  : Sand
# @FileName: 2.10086示例.py
# @Project : OldBoy

message = """欢迎致电10086
1. 话费查询；
2. 流量服务；
3. 业务办理；
4. 人工服务"""

print(message)
index = input("请输入您要选择的服务：")
index = int(index)
if index == 1:
    print('话费查询')
elif index == 2:
    print('流量服务')
elif index == 3:
    content = """业务办理
    1. 修改密码；
    2. 更改套餐；
    3. 停机；"""
    print(content)
    value = input('请输入要办理的业务：')
    value = int(value)
    if value == 1:
        print('修改密码')
    elif value == 2:
        print('更改套餐')
    elif value == 3:
        print('停机')
    else:
        print('错误')
elif index == 4:
    print('人工服务')
else:
    print('输入错误')

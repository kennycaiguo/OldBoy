#!usr/bin/env python
# coding:utf-8
# @author: sand
# @file: 购物车.py
# @time: 2019/05/15


"""
基本需求：75%
1. 启动程序后，输入用户名密码后，让用户输入工资，然后打印商品列表
2. 允许用户根据商品编号购买商品
3. 用户选择商品后，检测余额是否够，够就直接扣款，不够就提醒
4. 可随时退出，退出时，打印已购买商品和余额
5. 在用户使用过程中， 关键输出，如余额，商品已加入购物车等消息，需高亮显示

升级需求：10%
1. 用户下一次登录后，输入用户名密码，直接回到上次的状态，即上次消费的余额什么的还是那些，再次登录可继续购买
2. 允许查询之前的消费记录
"""

goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998}
]
print(len(goods))
# user = input("请输入用户名：").strip()
# pwd = input("请输入密码：").strip()
#
# salary = int(input("请输入薪水：").strip())
print("商品列表".center(50, '-'))
for g in range(0, len(goods)):
    print("【编号：%d 商品：%s 价格：%d】" % (g, goods[g]["name"], goods[g]["price"]))


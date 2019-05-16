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

# account_data = {
#     "account" : ["Sand", "123456", 0],
#     "shopping_cart" : [],
#     "balance" : 5000
# }

file_name = 'data'

f = open(file_name, 'r', encoding='utf8')
account_data = eval(f.read())

user = input("请输入用户名：").strip()
pwd = input("请输入密码：").strip()
if user == account_data["account"][0] and pwd == account_data["account"][1]:
    while True:
        print("商品列表".center(50, '-'))
        for index in range(0, len(goods)):
            print("【编号：%d 商品：%s 价格：%d】" % (index, goods[index]["name"], goods[index]["price"]))

        choice = input("选择商品>：").strip()
        if choice.isdigit():
            choice = int(choice)
            if choice >= 0 and choice < len(goods):
                g = goods[choice]
                if g["price"] <= account_data["balance"]:
                    account_data["shopping_cart"].append(g)
                    account_data["balance"] -= g["price"]
                    print("添加商品[%s]到购物车，还有余额\033[1;31m%s\033[0m" % (g, account_data["balance"],))
                else:
                    print("余额不足。")
            else:
                print("无此商品。")
        elif choice == 'q':
            print("购物车".center(50, '-'))
            for i in account_data["shopping_cart"]:
                print(i)
            print("余额：%s" % account_data["balance"])
            f = open(file_name, 'w', encoding='utf8')
            f.write(str(account_data))
            f.close()
            exit("再见！")
else:
    print("用户名或者密码错误")

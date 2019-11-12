#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/1 10:18
# @Author  : Sand
# @FileName: app.py
# @Project : OldBoy
"""
有如下商品列表GOODS_LIST，用户可以选择进行购买商品并加入到购物车SHOPPING_CART中,且可以选择购买数量，
购买完成后将购买的所有商品写入到文件中，【文件格式：年_月__日.txt】
注意：重复购买同一件商品时，只更改购物车中的数量。
"""
from datetime import datetime

# 购物车
SHOPPING_CART = {}

# 商品列表
GOODS_LIST = [
    {'id': 1, 'title': '飞机', 'price': 1000},
    {'id': 3, 'title': '大炮', 'price': 1000},
    {'id': 8, 'title': '迫击炮', 'price': 1000},
    {'id': 9, 'title': '坦克', 'price': 1000}
]


def run():
    while True:
        for i in range(len(GOODS_LIST)):
            print(i + 1, GOODS_LIST[i]['title'])

        choice = input('请选择序号（N购买完成）：')
        if choice.upper() == 'N':
            # 购买完成之后，写入文件
            ctime = datetime.now().strftime('%Y-%m-%d')
            with open(ctime, mode='a', encoding='utf-8') as f:
                for key, value in SHOPPING_CART.items():
                    line = "%s|%s|%s|%s|\n" % (key, value['title'], value['price'], value['count'],)
                    f.write(line)
            break

        choice = int(choice)
        number = int(input('购买数量：'))
        row_info = GOODS_LIST[choice - 1]
        if row_info['id'] in SHOPPING_CART:
            SHOPPING_CART[row_info['id']]['count'] = SHOPPING_CART[row_info['id']]['count'] + number
        else:
            SHOPPING_CART[row_info['id']] = {'title': row_info['title'], 'price': row_info['price'], 'count': number}
        print(SHOPPING_CART)


if __name__ == '__main__':
    run()

#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/1 11:26
# @Author  : Sand
# @FileName: app.py
# @Project : OldBoy
"""
功能：
        1.用户注册，提示用户输入用户名和密码，然后获取当前注册时间，最后将用户名、密码、注册时间存入文件
        2.用户登录，只有3次错误机会，一旦错误则冻结账户（下次启动也无法登录，提示：用户已冻结）
        3.商品浏览，分页显示商品（小文件）；用户可以选择商品且可以选择数量然后加入购物车（在全局变量操作）
          不再购买之后，需要将购物信息写入到文件，文件要写入到指定目录：
                shopping_cart（文件夹）
                        - 用户名A（文件夹）
                                2019-11-11-09-59.txt
                                2019-11-12-11-56.txt
                                2019-11-11-11-47.txt
                        - 用户名B（文件夹）
                                2019-11-11-09-59.txt
                                2019-11-12-11-56.txt
                                2019-11-11-11-47.txt
          注意：重复购买同一件商品时，只更改购物车中的数量。
        4.我的购物车，查看用户所有的购物车记录，即：找到shopping_cart目录下当前用户所有的购买信息，并显示：
                2019-11-11-09-59.txt
                        飞机|1000|10个
                        大炮|2000|3个
                2019-11-12-09-59.txt
                        飞机|1000|10个
                        大炮|2000|3个
        5.用户未登录的情况下，如果访问商品流程、我的购物车时，提示登录之后才能访问，让用户先去选择登录（装饰器实现）

"""
import sys
import os
from datetime import datetime

CURRENT_USER = None


def auth(func):
    def inner(*args, **kwargs):
        if not CURRENT_USER:
            print('用户未登录，请登陆后再查看')
            return None
        return func(*args, **kwargs)

    return inner


@auth
def cart():
    folder_path = os.path.join('shopping_cart', CURRENT_USER)
    if not os.path.exists(folder_path):
        print('购物车为空')
        os.makedirs(folder_path)
        return

    for path in os.listdir(folder_path):
        print(path)
        file_path = os.path.join(folder_path, path)
        with open(file_path,mode='r',encoding='utf-8') as f:
            for line in f:
                print(line.strip())


@auth
def goods():
    """
    浏览并购买
    :return:
    """
    shopping_cart = {}
    while True:
        goods_list = []
        with open('goods.txt', mode='r', encoding='utf-8') as f:
            for line in f:
                nid, title, price = line.strip().split('|')
                goods_list.append({'id': nid, 'title': title, 'price': price})

        # 进行分页展示
        for i in range(len(goods_list)):
            print(i + 1, goods_list[i])

        choice = input('请选择(N不再购买)：')
        if choice.upper() == 'N':
            # 写入到购物车
            folder_path = os.path.join('shopping_cart', CURRENT_USER)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            ctime = datetime.now().strftime('%Y-%m-%d-%H-%M')
            file_path = os.path.join(folder_path, ctime)
            with open(file_path, mode='a', encoding='utf-8') as f:
                for key, value in shopping_cart.items():
                    line = "%s|%s|%s|%s|\n" % (key, value['title'], value['price'], value['count'],)
                    f.write(line)
            return

        choice = int(choice)
        number = int(input('请输入数量：'))
        row_dict = goods_list[choice - 1]

        if row_dict['id'] in shopping_cart:
            shopping_cart[row_dict['id']]['count'] += number
        else:
            shopping_cart[row_dict['id']] = {'title': row_dict['title'], 'price': row_dict['price'], 'count': number}


def register():
    """

    :return:
    """
    print('注册页面')
    while True:
        user = input('请输入用户（N退出）：')
        if user.upper() == 'N':
            return
        pwd = input('请输入密码：')
        create_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open('db.txt', mode='a', encoding='utf-8') as f:
            line = '%s|%s|%s\n' % (user, pwd, create_time)
            f.write(line)


def is_frozen(user):
    """
    判断用户名是否已经被冻结
    :param user: 要检查的用户名
    :return:
    """
    if not os.path.exists('frozen.txt'):
        return False
    with open('frozen.txt', 'r', encoding='utf-8') as f:
        user_list = f.readlines()
    frozen_user_list = {item.strip() for item in user_list if item.strip()}  # 集合查找速度比列表快
    if user in frozen_user_list:
        return True
    return False


def login():
    """
    :return:
    """
    print('用户登录')
    count = 0
    while True:
        user = input('请输入用户名：')
        pwd = input('请输入密码：')

        # 判断用户名是否已经冻结
        result = is_frozen(user)
        if result:
            print('用户名已经冻结')
            continue

        # 用户未被冻结，去db中查找用户密码是否正确
        flag = False
        username_exists = False
        if not os.path.exists('db.txt'):
            print('无用户，请注册！')
            return

        with open('db.txt', mode='r', encoding='utf-8') as f:
            for line in f:
                username, password, ctime = line.split('|')
                if username == user:
                    username_exists = True
                if username == user and password == pwd:
                    flag = True
                    print('登录成功')
                    global CURRENT_USER
                    CURRENT_USER = user
                    return

        if not username_exists:
            print('用户名不存在，请重新登录')
            continue

        if not flag:
            print('用户或密码错误')
            if count == 2:
                print('错误次数已经达到3次')
                with open('frozen.txt', 'a', encoding='utf-8') as f:
                    f.write(user + '\n')
                return
            count += 1


def run():
    func_dict = {'1': register, '2': login, '3': goods, '4': cart}
    while True:
        print('1.用户注册;2.用户登录;3.商品浏览;4.我的购物车')
        choice = input('请选择：')
        func = func_dict.get(choice)
        if not func:
            print('输入错误')
            continue
        func()


if __name__ == '__main__':
    run()

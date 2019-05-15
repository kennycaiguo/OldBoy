# -*- coding: utf-8 -*-
# @Time    : 2019/5/15 17:40
# @Author  : Sand
# @FileName: 三次登录作业.py
# @Project : OldBoy


'''
思路：（功能拆分，拼凑功能）
1. 先写登录
2. 再写3次循环
3. 在循环中嵌套登录
'''

count = 1
while count <= 3:
    user = input('请输入用户名：')
    pwd = input('请输入密码：')
    if user == 'oldboy' and pwd == 'alex':
        print('登录成功！')
    else:
        print('登录失败')
    if count == 3:
        choice = input('请输入是否继续（Y/N）：')
        if choice == 'N':
            break
        elif choice == 'Y':
            count = 1
            continue
        else:
            print('输入错误')
            break
    count += 1
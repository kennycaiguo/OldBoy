# -*- coding: utf-8 -*-
# @Time    : 2019/5/15 11:18
# @Author  : Sand
# @FileName: 作业.双色球.py
# @Project : OldBoy

"""
作业1：双色球选购
1 双色球（假设一共八个球，6个红球，球号1-32、2个蓝球，球号1-16）
2 确保用户不能重复选择，不能超出范围
3 用户输入有误时有相应的错误提示
4 最后展示用户选择的双色球的号码
"""

red_ball_poll = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
                 29,
                 30, 31, 32]
blue_ball_poll = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

red_ball = []
count = 1
print('Welcome to the lottery station!')
# print(red_ball_poll)
while True:
    red = int(input('\033[1;31m[%d]select red ball:\033[0m' % (count,)).strip())
    if red in red_ball_poll:
        if red not in red_ball:
            red_ball.append(red)
            count += 1
        else:
            print("number %d is already exist in red ball list" % (red,))
    else:
        print('only can select n between 1-32')
    if count > 6:
        count = 1
        break

blue_ball = []
# print(blue_ball_poll)
while True:
    blue = int(input('\033[1;34m[%d]select blue ball:\033[0m' % (count,)).strip())
    if blue in blue_ball_poll:
        if blue not in blue_ball:
            blue_ball.append(blue)
            count += 1
        else:
            print("number %d is already exist in blue ball list" % (blue,))
    else:
        print('only can select n between 1-16')
    if count > 2:
        break

print("red ball:", end=" ")
print(red_ball)
print("blue ball:", end=" ")
print(blue_ball)
exit("Good Luck")

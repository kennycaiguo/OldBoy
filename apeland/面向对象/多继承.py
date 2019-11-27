#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/13 10:51
# @Author  : Sand
# @FileName: 多继承.py
# @Project : OldBoy


class Shenxian:
    """神仙类"""

    def fly(self):
        print("神仙都会飞。。。。")

    def fight(self):
        print("神仙打架。。。")


class Monkey:

    def eat_peach(self):
        print("猴子都喜欢吃桃子。。。")

    def fight(self):
        print("猴子在打架。。。")


class MonkeyKing(Shenxian, Monkey):

    def play_golden_stick(self):
        print("孙悟空玩金箍棒。。。")


swk = MonkeyKing()
swk.play_golden_stick()
swk.fly()
swk.eat_peach()
swk.fight()

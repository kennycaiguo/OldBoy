#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/31 18:13
# @Author  : Sand
# @FileName: app.py
# @Project : OldBoy

"""
大文件分页
"""


def run():
    """
    主函数
    :return: 
    """""
    while True:
        num = int(input('请选择页码：'))
        per_page_count = 10
        # 每页显示10条数
        start = (num - 1) * per_page_count
        end = num * per_page_count

        result = []
        count = 0
        with open('db.txt', 'r', encoding='utf-8') as f:
            first_line = f.readline()
            for line in f:
                if count == end:
                    break
                if count >= start:
                    result.append(line)

                count += 1
        for i in range(len(result)):
            print(i + 1, result[i])


if __name__ == '__main__':
    run()

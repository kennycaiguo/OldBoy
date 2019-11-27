# -*- coding: utf-8 -*-
# @Time    : 2019/5/14 15:51
# @Author  : Sand
# @FileName: 5.运算符.py
# @Project : OldBoy


# 练习题：打印1-100里面的奇数

# number = 1
# while number <= 100:
#     value = number % 2
#     if value > 0:
#         print(number)
#     number = number + 1

# value = 2**8
# print(value)

# value = 11 // 3
# print(value)

# 练习题：1-100相加的和
# count = 1
# sum = 0
# while count <= 100:
#     sum = sum + count
#     count = count + 1
#
# print(sum)


############逻辑运算###############
"""
1. 数字转字符串
2. 字符串转数字
3. "" 和 0 转换布尔值都为False，其他为True
"""


##面试题
"""
对于or，如果有遇到：
    value = 1 or 9
    如果第一个值转换成布尔值是真，则value=第一个，
    如果第一个值转换成布尔值是假，则value=第二个，
    如果有多个or，就从左到右依次进行上述流程。
    示例：
        val1 = 1 or 9
        val2 = 0 or 9
        val3 = 0 or ""
        print(val1)
        print(val2)
        print("--->", val3, "<---")
        value = 0 or 9 or 8     #从左往右算 0 or 9 = 9， 9 or 8 = 9
        print(value)    
"""

# 对于and，如果遇到，
"""
    如果第一个值转换成布尔值是True，则value=第二个值，
    如果第一个值转换成布尔值是False，则value=第一个值，
    如果有多个and，就从左到右依次进行上述流程。
    示例：
        val1 = 1 and 9
        val2 = 1 and 0
        val3 = 0 and 7
        val4 = 0 and ""
        val5 = 1 and 0 and 9
        print(val5)  
"""

# 综合
# 先看and再看or
value = 1 and 9 or 0 and 6
print(value)

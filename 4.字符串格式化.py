# -*- coding: utf-8 -*-
# @Time    : 2019/5/14 15:02
# @Author  : Sand
# @FileName: 4.字符串格式化.py
# @Project : OldBoy

"""
name = input('姓名：')
do = input('在干什么：')
template = "%s在教室，%s。"%(name, do,)
print(template)
"""

"""
template = "我是%s，年龄%d，职业%s。" %("alex", 73, "讲鸡汤",)
print(template)
"""

# name = "alex"
# template = "%s现在手机的电量是100%%" %(name,)
# print(template)

# 练习

name = input("请输入姓名：")
age = input("请输入年龄：")
job = input("请输入职业：")
hobby = input("请输入爱好：")
msg = '''
------------info of Alex Li-----------
Name : %s
Age  : %s
Job  : %s
Hobby: %s
-------------End----------------------
'''
data = msg %(name, age, job, hobby,)
print(data)
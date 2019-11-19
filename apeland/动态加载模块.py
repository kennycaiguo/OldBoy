#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/19 16:58
# @Author  : Sand
# @FileName: 动态加载模块.py
# @Project : OldBoy


# __import__("property")  # 解释器用的

import importlib

importlib.import_module("property")  # 官方推荐
importlib.import_module("apeland.property")  # 官方推荐

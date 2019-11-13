#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/13 15:47
# @Author  : Sand
# @FileName: 多态2.py
# @Project : OldBoy


class Document:
    def __init__(self, name):
        self.name = name

    def show(self):
        raise NotImplementedError("Subclass must implement abstract method")  # 调用这个方法的时候，必须在子类重写


class Pdf(Document):
    def show(self):
        return 'Show PDF contents'


class Word(Document):
    def show(self):
        return "Show word contents"


pdf_obj = Pdf("嫩模联系方式.pdf")
word_obj = Word("护士联系方式.doc")

print(pdf_obj.show())
print(word_obj.show())

objs = [pdf_obj, word_obj]
for o in objs:
    print(o.name + ':' + o.show())

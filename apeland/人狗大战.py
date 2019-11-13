#!usr/bin/env python
# coding:utf-8
# @author: sand
# @file: 人狗大战.py
# @time: 2019/11/11


class Dog:
    role = 'dog'

    def __init__(self, name, breed, attack_val):
        self.name = name
        self.breed = breed
        self.hp = 100
        self.attack_val = attack_val

    def bite(self, person):
        person.hp -= self.attack_val
        print("%s狗咬啦人%s一口，人掉了%s的血，还有%s血量" % (self.name, person.name, self.attack_val, person.hp,))


class Person:
    role = 'person'
    
    def __init__(self, name, age, sex, attack_val):
        self.name = name
        self.age = age
        self.sex = sex
        self.hp = 100
        self.attack_val = attack_val

    def attack(self, dog):
        dog.hp -= self.attack_val
        print("%s人打了狗%s一棒，狗掉了%s的血，还有%s血量" % (self.name, dog.name, self.attack_val, dog.hp,))


d1 = Dog('mike', '二哈', 30)
p1 = Person('Owen', 23, "M", 40)
d1.bite(p1)
p1.attack(d1)
d1.bite(p1)
p1.attack(d1)

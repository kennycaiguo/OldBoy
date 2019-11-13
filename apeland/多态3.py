#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/13 15:58
# @Author  : Sand
# @FileName: 多态3.py
# @Project : OldBoy


class Car:
    def __init__(self, name):
        self.name = name

    def drive(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def stop(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Truck(Car):

    def __init__(self, name):                   # 如果想调用父类的初始化方法，可以用以下3种
        # Car.__init__(self, name)
        # super(Truck, self).__init__(name)
        super().__init__(name)                  # 一般都是用这种写法

    def drive(self):
        print("Truck is running...")

    def stop(self):
        print("Truck is stopped...")


class SportCar(Car):

    def __init__(self, name):
        super().__init__(name)

    def drive(self):
        print("SportCar is running...")

    def stop(self):
        print("SportCar is stopped...")


t = Truck('三菱重卡')
sc = SportCar('保时捷')

cars = [t,sc]
for car in cars:
    print(car.name)
    car.drive()
    car.stop()

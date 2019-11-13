#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/13 16:27
# @Author  : Sand
# @FileName: 校园IT管理系统.py
# @Project : OldBoy


from datetime import datetime


class School(object):
    def __init__(self, name, addr):
        self.name = name
        self.addr = addr
        self.staff_objs = []
        self.student_objs = []
        self.school_balance = 100000
        print("初始化【%s】成功！地址：【%s】" % (self.name, self.addr,))

    def pay_roll(self, staff_objs):
        total = 0
        for staff in staff_objs:
            total += staff.get_salary()
        self.school_balance -= total
        create_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(create_time + "%s发工资，账户余额:%s" % (total, self.school_balance))

    def count_staff_num(self):
        print("员工人数为：", len(self.staff_objs))
        return self.staff_count

    def count_student_num(self):
        print("学员人数：", len(self.student_objs))
        return self.student_count

    def new_staff_enrollment(self, staff_obj):
        self.staff_objs.append(staff_obj)
        create_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(create_time + " 员工注册成功，员工姓名：【%s】，年龄：【%s】，职务：【%s】，校区：【%s】" % (
            staff_obj.name, staff_obj.age, staff_obj.position, self.name))

    def new_student_enrollment(self, student_obj):
        self.student_objs.append(student_obj)
        create_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(create_time + "学员注册成功，学员信息")


class BranchSchool(School):
    def __init__(self, name, addr):
        super().__init__(name, addr)
        self.head_quater = None


class Course(object):
    def __init__(self, name, price, outline):
        self.name = name
        self.__price = price
        self.outline = outline

    def get_course_price(self):
        return self.__price

    def update_course_price(self, price):
        self.__price = price


class Class(object):
    def __init__(self, name, course_obj, school_obj):
        self.class_name = name
        self.course_obj = course_obj
        self.school_obj = school_obj

    def create_teaching_record(self):
        create_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(create_time + "上什么课程" + self.course_obj.name)

    def drop_out(self, student):
        create_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.school_obj.student_objs.pop(student)
        print(create_time + "%s班级的[%s]学员退学" % (self.class_name, student.name))
        print("[%s]校区当前学院数：%s" % (self.school_obj.name, len(self.school_obj.student_objs)))


class Student(Class):
    def __init__(self, name, age, degree, class_obj, balance):
        self.name = name
        self.age = age
        self.degree = degree
        self.class_obj = class_obj
        self.__balance = balance

    def pay_tuition(self):
        self.__balance -= self.course_obj.price
        self.school_obj.balance += self.course_obj.price
        create_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(create_time + "[%s]学员交学费" % (self.name,))
        return self.get_balance()

    def get_balance(self):
        return self.__balance


class Staff(object):
    def __init__(self, name, age, position, salary, dept, school_obj):
        self.name = name
        self.age = age
        self.position = position
        self.__salary = salary
        self.dept = dept
        self.school_obj = school_obj

    def count_school_balance(self):
        return self.school_obj.school_balance

    def get_salary(self):
        return self.__salary


class Teacher(Staff):
    def __init__(self, name, age, salary, dept, school_obj):
        super().__init__(name, age, salary, dept, school_obj, position='teacher')

    def teaching(self, course_obj):
        print("[%s]老师正在教授[%s]" % (self.name, course_obj.name))


if __name__ == '__main__':
    school1 = School("崇仁路小学", "硚口区崇仁路")
    staff1 = Staff('Sand', 33, "校长", 3000, '校长办公室', school1)
    staff2 = Staff('Summery', 33, "主任", 3000, '政教办公室', school1)
    staff3 = Staff("Cathy", 29, "财务", 1000, '财务办公室', school1)
    school1.new_staff_enrollment(staff1)
    school1.new_staff_enrollment(staff2)
    school1.new_staff_enrollment(staff3)

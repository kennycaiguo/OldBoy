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
        self.branches = {}
        self.__staff_list = []
        self.__school_balance = 100000
        print("初始化校区[%s],地址:%s..." % (self.name, self.addr))

    def pay_roll(self, staff_list):
        total = 0
        for staff in staff_list:
            total += staff.get_salary()
        self.__school_balance -= total
        create_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(create_time + "%s发工资，账户余额:%s" % (total, self.__school_balance))

    def count_staff_num(self):
        """统计公司各分校员工人数"""
        total_staff_num = len(self.__staff_list)  # 当前校区员工数
        for i in self.branches:
            total_staff_num += len(self.branches[i].__staff_list)
        print("[%s]总员工数量:%s" % (self.name, total_staff_num))
        return total_staff_num

    def get_staff_num(self):
        return len(self.__staff_list)

    def count_student_num(self):
        print("学员人数：", len(self.student_list))
        return len(self.student_list)

    def new_staff_enrollment(self, staff_obj):
        self.__staff_list.append(staff_obj)
        create_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(create_time + " 员工注册成功，员工姓名：【%s】，年龄：【%s】，职务：【%s】，校区：【%s】" % (
            staff_obj.name, staff_obj.age, staff_obj.position, self.name))

    def count_total_balance(self):
        balance = self.__school_balance
        for branch_name, branch_obj in self.branches.items():
            balance += branch_obj.__school_balance
        print("Total balance:", balance)


class BranchSchool(School):
    def __init__(self, name, addr, head_quater_obj):
        super().__init__(name, addr)
        self.head_quater = head_quater_obj
        self.head_quater.branches[name] = self


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
    def __init__(self, class_num, start_date, course_obj, school_obj):
        self.class_num = class_num
        self.start_date = start_date
        self.course_obj = course_obj
        self.school_obj = school_obj
        self.stu_list = []
        print("校区[%s]开设了[%s]课程第[%s]班,开班日期[%s]..." % (school_obj.name, course_obj.name, class_num, start_date))

    def get_class_name(self):
        return "%s-%s-s%s期" % (self.school_obj.name, self.course_obj.name, self.class_num)

    def new_student_enrollment(self, student_obj):
        self.stu_list.append(student_obj)
        create_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(create_time + "学员注册成功，学员信息")

    def create_teaching_record(self):
        create_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(create_time + "上什么课程" + self.course_obj.name)

    def drop_out(self, stu_obj):
        create_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.stu_list.remove(stu_obj)
        print(create_time + "学员[%s]从[%s]退学了...." % (stu_obj.name, self.get_class_name()))
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
    def __init__(self, name, age, salary, dept, school_obj, position):
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
    head_quater = School("崇仁路小学", "硚口区崇仁路")
    staff1 = Staff('Sand', 33, 3000, '校长办公室', head_quater, "校长")
    staff2 = Staff('Summery', 33, 3000, '政教办公室', head_quater, '主任')
    staff3 = Staff("Cathy", 29, 1000, '财务办公室', head_quater, '财务')
    t1 = Teacher('王泽宇', 33, 9000, '语文组', head_quater)
    t2 = Teacher('雷锋', 33, 10000, '英语组', head_quater)
    t3 = Teacher('二蛋', 33, 9000, '数学组', head_quater)
    head_quater.new_staff_enrollment(staff1)
    head_quater.new_staff_enrollment(staff2)
    head_quater.new_staff_enrollment(staff3)
    head_quater.new_staff_enrollment(t1)
    head_quater.new_staff_enrollment(t2)
    head_quater.new_staff_enrollment(t3)

    b1 = BranchSchool('崇仁路小学汉西分校', '硚口区汉西路', head_quater)
    staff4 = Staff("VC", 29, 2000, '总务处', b1, "校长")
    staff5 = Staff("二哈", 49, 800, '保卫处', b1, "门房")
    staff6 = Staff("赵卫国", 39, 1000, '后勤', b1, "厨师")
    t4 = Teacher('黄潇', 23, 9000, '体育组', b1)
    t5 = Teacher('催锋', 53, 10000, '英语组', b1)
    t6 = Teacher('鬼见愁', 33, 7000, '数学组', b1)
    t7 = Teacher('李宗盛', 37, 8000, '音乐组', b1)
    b1.new_staff_enrollment(staff4)
    b1.new_staff_enrollment(staff5)
    b1.new_staff_enrollment(staff6)
    b1.new_staff_enrollment(t4)
    b1.new_staff_enrollment(t5)
    b1.new_staff_enrollment(t6)
    b1.new_staff_enrollment(t7)

    head_quater.count_staff_num()
    b1.count_staff_num()

    head_quater.count_total_balance()
    b1.count_total_balance()

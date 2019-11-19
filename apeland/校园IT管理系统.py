#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/13 16:27
# @Author  : Sand
# @FileName: 校园IT管理系统.py
# @Project : OldBoy


from datetime import datetime


class School(object):
    """总部/学校类"""

    def __init__(self, name, addr, website):
        self.name = name
        self.addr = addr
        self.website = website
        self.branches = []
        self.class_list = []  # 存班级列表
        self.staff_list = []
        self.balance = 0
        print("初始化校区【%s】,地址:%s..." % (self.name, self.addr))

    def pay_roll(self):
        print("开始发11月份的工资啦。。。。")
        for staff in self.staff_list:
            staff.balance += staff.salary
            self.balance -= staff.salary
            create_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(create_time + " 给%s发了%s工资，他的账户余额:%s" % (staff.name, staff.salary, staff.balance))
        print("公司余额：", self.balance)

    def count_staff_num(self):
        """统计公司各分校员工人数"""
        total_staff_num = len(self.staff_list)  # 当前校区员工数
        for i in self.branches:
            total_staff_num += len(self.branches[i].staff_list)
        print("[%s]总员工数量:%s" % (self.name, total_staff_num))
        return total_staff_num

    def count_student_num(self):
        print("学员人数：", len(self.student_list))
        return len(self.student_list)

    def new_staff_enrollment(self, staff_obj):
        self.staff_list.append(staff_obj)
        create_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(create_time + " 员工注册成功，员工姓名：【%s】，年龄：【%s】，职务：【%s】，校区：【%s】" % (
            staff_obj.name, staff_obj.age, staff_obj.position, self.name))

    def count_class_list(self):
        print("-----各校区班级-----")
        print(self.name, self.class_list)
        for i in self.branches:
            print(i.name, i.class_list)

    def count_total_revenue(self):
        print("-----校区总收入-----")
        total_rev = self.balance
        print(self.name, self.balance)
        for b in self.branches:
            print(b.name, b.balance)
            total_rev += b.balance
        print("各校区总收入:%s" % (total_rev,))

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class BranchSchool(School):
    """分校"""

    def __init__(self, name, addr, website, head_quarter_obj):
        super().__init__(name, addr, website)
        self.head_quarter = head_quarter_obj
        self.head_quarter.branches.append(self)  # 把自己加入到总校的校区列表李，建立总部-》分校的反向关联


class Course(object):
    """课程类"""

    def __init__(self, name, price, outline):
        self.name = name
        self.price = price
        self.outline = outline
        print("创建了课程【%s】，学费【%s】" % (name, price))


class Class(object):
    """班级"""

    def __init__(self, course_obj, semester, school_obj):
        self.course_obj = course_obj
        self.semester = semester
        self.school_obj = school_obj
        self.stu_list = []  # 存放学员列表

        school_obj.class_list.append(self)  # 把自己加到校区的班级列表
        print("校区【%s】创建了班级【%s】学期【%s】..." % (school_obj.name, course_obj.name, semester))

    def stu_transfer(self, stu_obj, new_class_obj):
        """
        学员转校
        :param stu_obj: 学员对象
        :param new_class_obj: 转到新的班级的对象
        :return:
        """
        pass

    def __str__(self):
        """返回一个对象的描述信息"""
        return "%s-%s-%s学期" % (self.school_obj.name, self.course_obj.name, self.semester)

    def __repr__(self):
        """返回一个对象的描述信息"""
        return "%s-%s-%s学期" % (self.school_obj.name, self.course_obj.name, self.semester)

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


class Student(object):
    """学员"""

    def __init__(self, name, age, balance, class_obj):
        self.name = name
        self.age = age
        self.balance = balance
        self.class_obj = class_obj

        # 加入班级
        class_obj.stu_list.append(self)
        # 交学费
        class_obj.school_obj.balance += class_obj.course_obj.price
        self.balance -= class_obj.course_obj.price
        print('班级【%s】加入了新学员【%s】，交了学费【%s】' % (class_obj, name, class_obj.course_obj.price,))

    def punch_card(self):
        ctime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print("%s：学员在班级【%s】上课了。。。" % (ctime, self.class_obj))


class Staff(object):
    """员工"""

    def __init__(self, name, age, balance, salary, position, dept, school_obj):
        self.name = name
        self.age = age
        self.balance = balance
        self.salary = salary
        self.position = position
        self.dept = dept
        self.school_obj = school_obj

        school_obj.new_staff_enrollment(self)  # 办入职

    def punch_card(self):
        pass

    def count_school_balance(self):
        return self.school_obj.balance


class Teacher(Staff):
    def __init__(self, name, age, balance, salary, position, dept, school_obj, course_obj):
        super().__init__(name, age, balance, salary, position, dept, school_obj)
        self.course_obj = course_obj  # 老师可以讲的课程

    def teach_class(self, class_obj, day):
        print("【%s】老师正在班级【%s】上第【%s】天课ing" % (self.name, class_obj, day))


if __name__ == '__main__':
    # 创建校区
    head_quarter = School("崇仁路小学", "硚口区崇仁路", "master.com")
    sh1_school = BranchSchool("崇仁路小学汉西分校", "硚口区汉西路", "master.com", head_quarter)
    sh2_school = BranchSchool("崇仁路小学古田分校", "硚口区古田", "master.com", head_quarter)
    sz1_school = BranchSchool("崇仁路小学洪山分校", "洪山亚贸", "master.com", head_quarter)
    sz2_school = BranchSchool("崇仁路小学青山分校", "青山八大家", "master.com", head_quarter)

    # 创建课程
    py_course = Course("Python", 21800, None)
    linux_course = Course("Python", 19800, None)
    test_course = Course("Python", 19800, None)
    go_course = Course("Python", 22800, None)

    # 创建班级
    py_24 = Class(py_course, 24, head_quarter)
    py_12 = Class(py_course, 12, sh1_school)
    linux_63 = Class(linux_course, 63, sz1_school)
    go_5 = Class(go_course, 5, head_quarter)

    # 创建员工、老师、学员
    s1 = Staff('Sand', 33, 0, 3000, "校长", '校长办公室', head_quarter)
    s2 = Staff('Summery', 33, 0, 3000, '主任', '政教办公室', head_quarter)
    s3 = Staff("Cathy", 29, 0, 1000, '财务', '财务办公室', head_quarter)
    s4 = Staff("VC", 29, 0, 2000, "校长", '总务处', sh1_school)
    s5 = Staff("二哈", 49, 0, 800, "门房", '保卫处', sz1_school)
    s6 = Staff("赵卫国", 39, 0, 1000, "厨师", '后勤', sz2_school)

    t1 = Teacher('王泽宇', 33, 0, 9000, "讲师", '语文组', sh1_school, py_course)
    t2 = Teacher('雷锋', 33, 0, 10000, "讲师", '英语组', sh1_school, go_course)
    t3 = Teacher('二蛋', 33, 0, 9000, "讲师", '数学组', sz1_school, linux_course)
    t4 = Teacher('黄潇', 23, 0, 9000, "讲师", '体育组', sh2_school, linux_course)
    t5 = Teacher('催锋', 53, 0, 10000, "讲师", '英语组', sh2_school, test_course)
    t6 = Teacher('鬼见愁', 33, 0, 7000, "讲师", '数学组', sz2_school, test_course)
    t7 = Teacher('李宗盛', 37, 0, 8000, "讲师", '音乐组', sz2_school, py_course)

    stu1 = Student("春生", 22, 50000, py_24)
    stu2 = Student("black girl", 26, 30000, go_5)
    stu3 = Student("小强", 22, 35000, go_5)
    stu3 = Student("小虎", 28, 38000, linux_63)

    print(head_quarter.balance)
    print(sz1_school.balance)

    print(head_quarter.branches)
    # 统计 账户余额、班级
    head_quarter.count_total_revenue()
    head_quarter.count_class_list()
    # 发工资
    head_quarter.pay_roll()
    sz1_school.pay_roll()
    sz2_school.pay_roll()
    sh1_school.pay_roll()

import random

from flask import Blueprint, request, render_template
from .models import *

# 蓝图
blue = Blueprint('user', __name__)
blue2 = Blueprint('product', __name__)

@blue.route('/')
def home():
    return "flask home"

# 多表操作
# 一对多
# 增加数据
@blue.route('/addgrade')
def add_grade_stu():
    # 添加班级
    grades = []
    for i in range(10):
        grade = Grade()
        grade.name = f'Jay{i}--{str(random.randint(10, 99))}'
        grades.append(grade)
    try:
        db.session.add_all(grades)
        db.session.commit()
    except Exception as e:
        print('e:', e)
        db.session.rollback()
        db.session.flush()
    return 'OK'

@blue.route('/addstu')
def add_stu():
    # 添加班级
    students = []
    for i in range(10):
        stu = Student()
        stu.name = f'Lucy{i}'
        stu.age = i
        stu.grade_id = random.randint(1, 3)
        students.append(stu)
    try:
        db.session.add_all(students)
        db.session.commit()
    except Exception as e:
        print('e:', e)
        db.session.rollback()
        db.session.flush()
    return 'OK'

# 修改
@blue.route('/updatestu/')
def update_stu():
    stu = Student.query.first()
    stu.age = 100
    db.session.commit()
    return 'OK'

# 删除
@blue.route('/delstu/')
def del_stu():
    stu = Student.query.first()
    db.session.delete(stu)
    db.session.commit()
    return 'OK'

@blue.route('/delgrade/')
def del_grade():
    grade = Grade.query.first()
    db.session.delete(grade)
    db.session.commit()
    return 'OK'

# 查询
@blue.route('/getstu/')
def get_stu():
    # 查询学生所在的班级， 反向引用grade
    stu = Student.query.get(2)
    print(stu.name , stu.age)
    print(stu.grade_id, stu.grade.name )
    # 查找班级下的所有学生
    grade = Grade.query.get(2)
    print(grade.name)
    print(grade.students) # 所有学生
    for stu in grade.students:
        print(stu.name, stu.age, stu.grade_id)
    return 'OK'
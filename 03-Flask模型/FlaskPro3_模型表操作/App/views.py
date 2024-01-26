from flask import Blueprint, request, render_template
from sqlalchemy import desc, or_, and_, not_

from .models import *

# 蓝图
blue = Blueprint('user', __name__)
blue2 = Blueprint('product', __name__)

@blue.route('/')
def home():
    return "flask home"

# 单表操作
# 增删改查
# 增：添加数据
@blue.route('/useradd/')
def user_add():
    # u = User()
    # u.name = 'kun'
    # u.age = 20
    # db.session.add(u)   # 将u对象添加到seesion中
    # db.session.commit() # 同步到数据库中


    # 同时添加多条数据
    users = []
    for i in range(10, 30):
        u = User()
        u.name = '冰冰' + str(i)
        u.age=i
        users.append(u)

    try:
        db.session.add_all(users)
        db.session.commit()  # 事务提交
    except Exception as e:
        db.session.rollback()   # 回滚  全部撤销
        db.session.flush()
        return 'fail:' + str(e)
    return 'success!'

# 删：删除数据
# 找到要删除的数据，然后删除
@blue.route('/userdel/')
def user_del():
    u = User.query.first() # 第一条数据
    db.session.delete(u)
    db.session.commit()
    return 'success!'

# 改：修改数据
# 找到要修改的数据，然后修改
@blue.route('/userupdate/')
def user_update():
    u = User.query.first()
    u.age = 1000
    db.session.commit()
    return 'success!'

# 查：查询数据
#   条件
@blue.route('/userget/')
def user_get():
    #users = User.query.all()

    # print(users)
    # print(User.query)

    # # filter（） 过滤
    # users = User.query.filter()
    # print(users, type(users))  # 查询集
    # print(list(users))
    #
    # # get()
    # user = User.query.get(8)
    # print(user, type(user))

    # filter() : 类似sql中的where
    # filter_by() ： 用于等值操作的过滤
    #users =User.query.filter(User.age==20)
    #users = User.query.filter_by(age=20)
    users = User.query.filter(User.age > 20)  # 可以用于非等值操作

    # first() : 第一条数据
    # last() : 最后一条数据
    user = User.query.first()
    # user = User.query.first_or_404()
    # print(list(users))
    # count() ： 统计查询集中的数据条数
    users = User.query.filter()
    #print(users.count())

    # limit() : 前几条
    # offset() : 跳过几条
    users = User.query.offset(3).limit(4)
    #print(list(users))

    # order_by() : 排序
    users = User.query.order_by('age')  #  升序
    users = User.query.order_by(desc('age'))  # 降序
    #print(list(users))

    # 逻辑运算: and_, or_, not_
    users = User.query.filter(User.age>20, User.age <25)
    users = User.query.filter(and_(User.age > 20, User.age < 25))
    users = User.query.filter(or_(User.age > 25, User.age < 20))

    # 查询属性 ： 名字中带了个 xxx  就把他找出来
    users = User.query.filter(User.name.contains('3'))

    # in() : 其中之一
    users = User.query.filter(User.age.in_(range(10, 30)))
    print(list(users))

    # startwith() : 以某子串开头
    # endwith() : 以某子串结尾
    users = User.query.filter(User.name.startwith('冰'))
    users = User.query.filter(User.name.endwith('2'))
    return 'success'

# 分页, 翻页
# 1. 手动翻页
#   offset.limit()
#   数据: 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20
#   页码: page =1
#   每页显示数量: per_page = 5
#   page=1 : 1,2,3,4,5       => offset(0).limit(5)
#   page=2 : 6,7,8,9,10      => offset(5).limit(5)
#   page=3 : 11,12,13,14,15  => offset(10).limit(5)
#   page=4 : 16,17,18,19,20  => offset(15).limit(5)
#   ...                         ...
#   page=n :                 => offset((page-1)*per_page).limit(5)

# 2. paginate 对象
@blue.route('/paginate/')
def get_paginate():
    # 页码:默认显示第一页
    page = int(request.args.get('page', 1))
    # per_page : 每页显示数据量
    per_page = int(request.args.get('per_page', 5))
    print(page, type(page))
    print(per_page, type(per_page))

    # paginate()
    p = User.query.paginate(page=page, per_page=per_page, error_out=False)
    print(p.items)
    # paginate 对象的属性
    #   items: 返回当前页的内容列表
    #   has_next: 是否还有下一页
    #   hax_prev: 是否还有上一页
    #   next(erro_out=False): 返回下一页的Pagination对象
    #   prev(erro_out=False): 返回上一页的pagination对象
    #   page: 当前页的页码(从1开始)
    print(p.page)
    #   pages: 总页数
    print(p.pages)
    #   per_page: 每页显示的数量
    #   prev_num: 上一页页码数量
    #   nexxt_num: 下一页页码数
    #   query: 返回创建该pagination对象的查询对象
    #   total： 查询返回的记录总数
    print(p.total)





    return render_template('paginate.html', p=p)
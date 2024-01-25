from flask import Blueprint
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
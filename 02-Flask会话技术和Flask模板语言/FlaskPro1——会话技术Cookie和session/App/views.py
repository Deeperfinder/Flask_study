import datetime

from flask import Blueprint, render_template, request, redirect, session
from .models import *

# 蓝图
blue = Blueprint('user', __name__)

# 首页
@blue.route('/')
@blue.route('/home/')
def home():
    # 4. 获取cookie
    #username = request.cookies.get('user')
    # 获取session
    username = session.get('user')
    return render_template('home.html', username=username)

# 登陆
@blue.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        # 1. 获取前端提交过来的数据
        username = request.form.get('username')
        password = request.form.get('password')

        # 2. 实现登陆功能 用户名和密码验证
        if username =='lisi' and password=='123':
            response = redirect('/home')

            # 3. 设置cookie
            # cookie 中不能用中文
            # response.set_cookie('user', username)  # 默认浏览器关闭，cookie失效
            # 过期时间
            # max_age:秒
            # expires: 指定的datatime日期
            # response.set_cookie('user', username, max_age=3600*24*7)
            #response.set_cookie('user', username, expires=datetime.datetime(2025, 1, 18))

            # 设置session
            session['user'] = username
            session.permanent=True
            return response
        else:
            return '用户名或密码错误'

# 注销
@blue.route('/logout/')
def logout():
    # 5. 删除cookie
    response = redirect('/home/')

    #response.delete_cookie('user')
    # 删除session
    session.pop('user')
    # session.clear() # 慎用，会删除服务器下所有session

    return response
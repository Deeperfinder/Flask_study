from flask import Blueprint, request, render_template, jsonify, make_response, Response, redirect
from .models import *

# 蓝图
blue = Blueprint('user', __name__)
blue2 = Blueprint('product', __name__)


@blue.route('/')
def home():
    return "flask home"


@blue.route('/string/<string:name>/')
def get_string(name):
    print(type(name))
    return name


# 请求与响应
@blue.route('/request/', methods=['POST', 'GET'])
def get_request():
    pass
    # get 请求参数
    # print(request)
    # print(request.method)
    # print(request.args)
    # print(request.args['name'])
    # print(request.args.getlist('name'))

    # post 请求参数
    # print(request.form)
    # print(request.form.get('name'))

    # cookie
    print(request.cookies)

    # 路径
    print(request.path)
    print(request.url)
    print(request.base_url)
    print(request.host_url)

    print(request.remote_addr)
    print(request.files)
    print(request.headers)

    print(request.user_agent)  # 用户代理，包括浏览器和操作系统信息
    return 'request ok'


# Respose： 服务器向客户端发送的响应
@blue.route('/response/')
def get_response():
    pass
    # 响应的几种方式
    # 1. 返回字符串(不常用)
    # return "request ok!"

    # 2. 模板渲染       （前后端不分离）
    # return render_template('index.html', name='张三', age=33)

    # 3. 返回json数据  （前后端分离）
    data = {'name': "李四", 'age': 44}
    # return data

    # jsonify() 序列化  将字典转为字符串
    # return jsonify(data=data)

    # 4. 自定义respose对象
    html = render_template('templates/index.html', name='张三', age=33)
    print(html)
    print(type(html))
    #res = make_response(html, 200)
    res = Response(html)
    return res

# 重定向
@blue.route('/redirect/')
def make_redirect():
    pass
    # 重定向的几种方式
    # return redirect("https://www.qq.com")
    return redirect('/response')

# 初始化文件
from flask import Flask, render_template
from .views import blue



def create_app():
    app = Flask(__name__)

    # 注册蓝图
    app.register_blueprint(blueprint=blue)
    return app
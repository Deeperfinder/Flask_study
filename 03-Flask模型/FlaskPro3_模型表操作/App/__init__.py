# 初始化文件
from flask import Flask, render_template
from .views import blue
from .exts import init_ext

def create_app():
    app = Flask(__name__)

    # 注册蓝图
    app.register_blueprint(blueprint=blue)

    # 配置数据库
    #db_uri = 'sqlite:///sqlite3.db'  # sqlite 配置

    db_uri = 'mysql+pymysql://root:123456@localhost:3306/flaskdb' #mysql 的配置
    app.config['SQLALCHEMY_DATABASE_URI'] =db_uri

    # 初始化插件
    init_ext(app=app)

    return app
# 初始化文件
from flask import Flask, render_template
from .views import blue


def create_app():
    app = Flask(__name__)

    # 注册蓝图
    app.register_blueprint(blueprint=blue)
    # session 配置
    print(app.config)
    '''<Config {'ENV': 'production', 'DEBUG': False, 'TESTING': False, 
    'PROPAGATE_EXCEPTIONS': None, 'SECRET_KEY': None, 
    'PERMANENT_SESSION_LIFETIME': datetime.timedelta(days=31), 
    'USE_X_SENDFILE': False, 'SERVER_NAME': None, 
    'APPLICATION_ROOT': '/', 'SESSION_COOKIE_NAME': 'session', 'SESSION_COOKIE_DOMAIN': None, 
    'SESSION_COOKIE_PATH': None, 'SESSION_COOKIE_HTTPONLY': True, 
    'SESSION_COOKIE_SECURE': False, 'SESSION_COOKIE_SAMESITE': None, 
    'SESSION_REFRESH_EACH_REQUEST': True, 'MAX_CONTENT_LENGTH': None, 'SEND_FILE_MAX_AGE_DEFAULT': None, 'TRAP_BAD_REQUEST_ERRORS': None, 'TRAP_HTTP_EXCEPTIONS': False, 'EXPLAIN_TEMPLATE_LOADING': False,  'PREFERRED_URL_SCHEME': 'http', 'JSON_AS_ASCII': None, 'JSON_SORT_KEYS': None, 'JSONIFY_PRETTYPRINT_REGULAR': None, 'JSONIFY_MIMETYPE': None, 'TEMPLATES_AUTO_RELOAD': None, 'MAX_COOKIE_SIZE': 4093}>
'''

    app.config['SECRET_KEY'] = 'abc123'

    return app
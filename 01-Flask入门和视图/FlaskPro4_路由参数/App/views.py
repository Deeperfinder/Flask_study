from flask import Blueprint
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
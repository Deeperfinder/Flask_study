from flask import Blueprint, render_template
from .models import *

# 蓝图
blue = Blueprint('user', __name__)
blue2 = Blueprint('product', __name__)

@blue.route('/')
def home():
    pass

    data = {
        'name': 'ikun ikun ikun',
        'age': 26,
        'likes': ['ball', 'sing', 'code', 'dance']
    }
    return render_template('child2.html', **data)

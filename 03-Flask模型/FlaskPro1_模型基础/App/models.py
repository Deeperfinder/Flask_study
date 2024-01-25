from .exts import db

# 模型    数据库
# 类     ==> 表结构
# 类属性  ==>  表字段
# 对象   ==>   表的一行数据



# 模型Model：类
class User(db.Model):
    # 表名
    __tablename__ = 'tb_user'
    # 定义 表的字段
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), unique=True, nullable=False, index=True)
    age = db.Column(db.Integer, default=1, nullable=False)
    sex = db.Column(db.Boolean, default=True, nullable=False)
    salary = db.Column(db.Float, default=100000, nullable=False)
    salary2 = db.Column(db.Float, default=100000, nullable=False)
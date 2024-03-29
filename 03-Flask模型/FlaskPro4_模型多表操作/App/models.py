from .exts import db


# 多表关系
# 一对多
# 班级：学生 = 1：N
# 班级表
class Grade(db.Model):
    __tablename__ = 'grade'  # 表的名字
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), unique=True)
    # 建立关联
    # 第1个参数: 关联的模型名 （表）
    # 第2个参数: 反向引用的名称，grade对象，让student反过来得到grade对象的名称:student.grade
    # 第3个参数: 懒加载
    students = db.relationship('Student', backref='grade', lazy=True)
    def __repr__(self):
        return self.name

# 学生表
class Student(db.Model):
    __tablename__ = 'student'  # 表的名字
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), unique=True)
    age = db.Column(db.Integer)
    # 外键 : 跟grade表中的id字段关联
    grade_id = db.Column(db.Integer, db.ForeignKey(Grade.id))



# ---------多对多-------

# 中间表: 收藏表
collect = db.Table(
    'collects',
    db.Column('user_id', db.Integer, db.ForeignKey('usermodel.id'), primary_key=True),
    db.Column('movie_id', db.Integer, db.ForeignKey('movie.id'), primary_key=True)
    )


# 用户 ： 电影 = N：M
# 用户表
class UserModel(db.Model):
    __tablename__ = 'usermodel'  # 表的名字
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30))
    age = db.Column(db.Integer)

# 电影表
class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30))
    age = db.Column(db.Integer)
    # 关联
    users = db.relationship('UserModel', backref='movies', lazy=True, secondary=collect)


from .exts import db

class User(db.Model):
    __tablename__ = 'user'  # 表的名字
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), unique=True)
    age = db.Column(db.Integer, default=1, nullable=False)

    def __repr__(self):
        return self.name
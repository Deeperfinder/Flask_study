# 插件管理
# 扩展的第三方插件
from flask_sqlalchemy import SQLAlchemy  # ORM
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()   # 数据迁移

def init_exts(app):
    db.init_app(app=app)
    migrate.init_app(app=app, db=db)
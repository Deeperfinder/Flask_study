### 数据迁移详细步骤 
1. 安装依赖
    flask-sqlalchemy 、 flask-migrate
2. 在exts.py文件中初始化Migrage和SQLAlchemy
3. 在modesl中定义模型
4. 在views.py中倒入models模块  
    from .models import *
5. 配置好数据库(sqlite3 或 mysql)   __init__.py
6. 执行数据迁移命令   
    6.1 在cmd或者terminal进入项目目录（app.py同级)  
    6.2 输入命令  
        `python3 -m flask db init` 创建迁移文件夹migrations  
         `python3 -m flask db migrate` 生成迁移文件  
        `python3 -m flask db upgrade` 执行迁移文件中的升级   
         `python3 -m flask db downgrade`  撤销升级
7. 查看数据库中的内容
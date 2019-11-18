from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from twittor.config import Config
from flask_mail import Mail

db = SQLAlchemy()   #建立数据库对象
migrate = Migrate() #建立数据库迁移对象
login_manager = LoginManager()  #建立flask_login对象
login_manager.login_view = 'login' # 设置当用户未登录时显示的页面
mail = Mail()

from twittor.route import index, login, logout, register,\
     user, page_not_found, edit_profile, reset_password_request,\
         password_reset, explore, user_activate

def create_app():
    app = Flask(__name__) #建立app对象
    app.config.from_object(Config)  # 从config.py中导入配置
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    mail.init_app(app)

    # 设置路由
    app.add_url_rule('/', 'index', index, methods=['GET', 'POST'])
    app.add_url_rule('/login', 'login', login, methods=['GET', 'POST'])
    app.add_url_rule('/logout', 'logout', logout)
    app.add_url_rule('/register', 'register', register, methods=['GET', 'POST'])
    app.add_url_rule('/<username>', 'profile', user, methods=['GET', 'POST'])
    app.add_url_rule('/edit_profile', 'edit_profile', edit_profile, methods=['GET', 'POST'])
    app.add_url_rule('/reset_password_request', 'reset_password_request', reset_password_request, methods=['GET', 'POST'])
    app.add_url_rule('/password_reset/<token>', 'password_reset', password_reset, methods=['GET', 'POST'])
    app.add_url_rule('/explore', 'explore', explore)
    app.add_url_rule('/activate/<token>', 'user_activate', user_activate)
    app.register_error_handler(404, page_not_found)
    return app


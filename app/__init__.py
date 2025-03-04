from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
# Модуль будет перенаправлять пользователя на маршрут, который мы указываем (на авторизацию)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

from app import routes
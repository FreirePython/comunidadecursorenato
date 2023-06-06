from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os


import config

app = Flask(__name__)

app.config['SECRET_KEY'] = 'f050ae9c4634d48182a7a336c23967bd'
if os.getenv("DATABASE_URL"):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db' Esse é o caminho para acessar o banco de dados local

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'alert-info'


from comunidadeimpressionadora import routes


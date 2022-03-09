from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
import pymysql
from os import getenv
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:password123@35.242.141.230:3306/flask_demo_db"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['SECRET_KEY'] = getenv('secret_key')
login_manager = LoginManager()
db = SQLAlchemy(app)
# login_manager.init_app(app)
# login manager.login_view ''
# @login_manager.user_loader
#def acquire_user(user_id):
 #   return User.query.get(user_id)

import application.routes

# return app


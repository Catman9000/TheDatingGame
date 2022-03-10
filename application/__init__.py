from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
import pymysql
from os import getenv
from flask_wtf import FlaskForm
from wtforms import validators


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = getenv('db_uri') # "mysql+pymysql://root:password123@35.242.141.230:3306/flask_demo_db"
# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['SECRET_KEY'] = "choochums"

db = SQLAlchemy(app)

from application import routes, forms, models
from flask import Flask
from application import app
from flask import request
from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from wtforms import validators

from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, RadioField, HiddenField, StringField, IntegerField, FloatField
from wtforms.validators import InputRequired, Length, Regexp, NumberRange, DataRequired
from datetime import date

class AddProduct(FlaskForm):
    product_name = StringField('Product name', validators=[DataRequired(message="This field cannot be left blank")])
    product_cost = IntegerField("Cost", validators=[DataRequired(message="This field cannot be left blank")])
    product_description = StringField("Product Description", validators=[DataRequired(message="This field cannot be left blank")])
    product_quantity = StringField("Product quantity", validators=[DataRequired(message="This field cannot be left blank")])
    submit = SubmitField("Add Item")

class UpdateProduct(FlaskForm):
    product_name = StringField('Product name', validators=[DataRequired(message="This field cannot be left blank")])
    product_cost = IntegerField("Cost", validators=[DataRequired(message="This field cannot be left blank")])
    product_description = StringField("Product Description", validators=[DataRequired(message="This field cannot be left blank")])
    product_quantity = StringField("Product quantity", validators=[DataRequired(message="This field cannot be left blank")])
    submit = SubmitField("Update Item")

class ChooseProduct(FlaskForm):
    chosenProduct = SelectField('Product', choices=[])
    submit = SubmitField("Choose Product")

class AddOrders(FlaskForm):
    order_placed = StringField('order placed', validators=[DataRequired(message="This field cannot be left blank")])
    order_total = IntegerField("Cost", validators=[DataRequired(message="This field cannot be left blank")])
    submit = SubmitField("Add Item")

class UpdateOrders(FlaskForm):
    order_placed = StringField('order placed', validators=[DataRequired(message="This field cannot be left blank")])
    order_total = IntegerField("Cost", validators=[DataRequired(message="This field cannot be left blank")])
    submit = SubmitField("Add Item")

class ChooseOrders(FlaskForm):
    order_placed = StringField('order placed', validators=[DataRequired(message="This field cannot be left blank")])
    order_total = IntegerField("Cost", validators=[DataRequired(message="This field cannot be left blank")])
    submit = SubmitField("Add Item")


class AddUser(FlaskForm):
    username = StringField('User name', validators=[DataRequired(message="This field cannot be left blank")])
    email = StringField("Email", validators=[DataRequired(message="This field cannot be left blank")])
    address = StringField("Address", validators=[DataRequired(message="This field cannot be left blank")])
    submit = SubmitField("Add User")

class AddCart(FlaskForm):
    username = SelectField("Name of user", choices=[])
    product_name = SelectField("Items", choices=[])
    submit = SubmitField("Create cart")

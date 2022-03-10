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
    submit = SubmitField("Add Item")

class UpdateProduct(FlaskForm):
    product_name = StringField('Product name', validators=[DataRequired(message="This field cannot be left blank")])
    product_cost = IntegerField("Cost", validators=[DataRequired(message="This field cannot be left blank")])
    product_description = StringField("Product Description", validators=[DataRequired(message="This field cannot be left blank")])
    submit = SubmitField("Update Item")

class ChooseProduct(FlaskForm):
    chosenProduct = SelectField('Product', choices=[])
    submit = SubmitField("Choose Product")


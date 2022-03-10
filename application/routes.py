from itertools import product
from flask import redirect, url_for, render_template, request
from application import app, db
from datetime import date, timedelta
from application.forms import AddProduct, UpdateProduct, ChooseProduct
from application.models import Product, user, Orders
from wtforms import validators

@app.route('/index', methods=["GET", "POST"])
@app.route("/", methods=["GET", "POST"])
def home():
   if request.form:
      print(request.form)
   return render_template('index.html')


@app.route('/add_an_item', methods=["GET", "POST"])
def add_an_item():
   form = AddProduct()
   if request.method == 'POST':
      product_name = form.product_name.data
      product_cost = form.product_cost.data
      product_description = form.product_description.data
      newProduct = Product(product_name = product_name, product_cost=product_cost, product_description = product_description)
      db.session.add(newProduct)
      db.session.commit()
   return render_template('add_an_item.html')

@app.route('/Shopping_Cart', methods=["GET", "POST"])
def Shopping_Cart():
   if request.form:
      print(request.form)
   return render_template('Shopping_Cart.html')
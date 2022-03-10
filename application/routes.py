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
   listofProducts= Product.query.all()
   return render_template("index.html", listofProducts=listofProducts)
  


@app.route('/add_an_item', methods=["GET", "POST"])
def add_an_item():
   listofProducts= Product.query.all()
   form = AddProduct()
   if request.method == 'POST':
      product_name = form.product_name.data
      product_cost = form.product_cost.data
      product_description = form.product_description.data
      product_quantity = form.product_quantity.data
      newProduct = Product(product_name = product_name, product_cost=product_cost, product_description = product_description, product_quantity=product_quantity)
      db.session.add(newProduct)
      db.session.commit()
   return render_template("add_an_item.html", listofProducts=listofProducts)

@app.route('/Shopping_Cart', methods=["GET", "POST"])
def Shopping_Cart():
   if request.form:
      print(request.form)
   return render_template('Shopping_Cart.html')


@app.route("/update", methods=["POST"])
def update():
    newquantity = request.form.get("newquantity")
    currentquantity = request.form.get("currentquantity")
    q = Product.query.filter_by(product_quantity=currentquantity).first()
    q.product_quantity = newquantity
    db.session.commit()
    return redirect("/")
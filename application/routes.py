from itertools import product
from flask import redirect, url_for, render_template, request
from application import app, db
from datetime import date, timedelta
from application.forms import AddProduct, UpdateProduct, ChooseProduct, AddUser, AddCart
from application.models import Product, user, orders
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


@app.route("/update", methods=["POST"])
def update():
    newquantity = request.form.get("newquantity")
    currentquantity = request.form.get("currentquantity")
    q = Product.query.filter_by(product_quantity=currentquantity).first()
    q.product_quantity = newquantity
    db.session.commit()
    return redirect("/")


@app.route("/delete", methods=["POST"])
def delete():
   product_name = request.form.get("product_name")
   p = Product.query.filter_by(product_name=product_name).first()
   db.session.delete(p)
   db.session.commit()
   return redirect("/")


@app.route('/add_user', methods=["GET", "POST"])
def add_user():
   form = AddUser()
   if request.method == 'POST':
      username = form.username.data
      email = form.email.data
      address = form.address.data
      newUser = user(username = username, email=email, address = address)
      db.session.add(newUser)
      db.session.commit()
   return render_template("add_user.html")


@app.route('/Shopping_Cart', methods=['GET', 'POST'])
def Shopping_Cart():
    User = user.query.all()
    product = Product.query.all()
    form = AddCart()
    form.username.choices.extend([(User.id, str(User)) for User in User])
    form.product_name.choices.extend([(product.id, str(product)) for product in product])
    if request.method == "POST":
        User = form.username.data
        product = form.product_name.data
        new_cart = orders(orderer=user, product_ordered=product)
        db.session.add(new_cart)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('Shopping_Cart.html', form=form, pageTitle="Create Cart")
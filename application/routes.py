from flask import redirect, url_for, render_template, request
from application import app, db
from datetime import date, timedelta
from application.models import user

@app.route('/index')
@app.route("/", methods=["GET", "POST"])
def home():
   if request.form:
        print(request.form)
   return render_template('index.html')



@app.route('/add_an_item')
@app.route("/", methods=["GET", "POST"])
def add_an_item():
   return render_template('add_an_item.html')

@app.route('/Shopping_Cart')
@app.route("/", methods=["GET", "POST"])
def Shopping_Cart():
   return render_template('Shopping_Cart.html')

@app.route('/your_reviews')
@app.route("/", methods=["GET", "POST"])
def your_reviews():
   return render_template('your_reviews.html')

@app.route('/Apply_for_job')
@app.route("/", methods=["GET", "POST"])
def Apply_for_job():
   return render_template('Apply_for_job.html')
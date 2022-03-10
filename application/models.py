from application import db
from sqlalchemy.orm import relationship

class user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(75))
    user_email = db.Column(db.String(75))
    user_address = db.Column(db.String(75))
    orders = db.relationship('Order', backref='person',
                            lazy='dynamic')


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_description = db.Column(db.String(150))
    product_cost = db.Column(db.Float(6,2))


class Product_Type(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_category = db.Column(db.String(150))
    products_id = db.Column(db.Integer, db.ForeignKey('Product.id'))

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_placed = db.Column(db.DATETIME)
    order_total = db.Column(db.Float(7,2))
    
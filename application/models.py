from application import db
from sqlalchemy.orm import relationship
from wtforms import validators

class user(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(75))
    email = db.Column(db.String(75))
    address = db.Column(db.String(75))
    orders = db.relationship('orders', backref='user',
                            lazy='dynamic')
    def __repr__(self):
        return f"{self.username}" 


class Product(db.Model):
    __tablename__ = 'Product'
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(150))
    product_description = db.Column(db.String(150))
    product_cost = db.Column(db.Numeric(6,2))
    product_quantity = db.Column(db.Integer)
    # fk_product_type_id = db.Column(db.Integer, db.ForeignKey('Product_Type.id'))
    def __repr__(self):
        return f"{self.product_name}"    

# class Product_Type(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     product_category = db.Column(db.String(150))
#     def __repr__(self):
#         return f"{self.product_category}"

class orders(db.Model):
    __tablename__ = ''
    id = db.Column(db.Integer, primary_key=True)
    orderer = db.Column(db.Integer, db.ForeignKey('user.id'))
    product_ordered = db.Column(db.Integer, db.ForeignKey('Product.id'))
  
    
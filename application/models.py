from application import db
from sqlalchemy.orm import relationship
from wtforms import validators

class user(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(75))
    user_email = db.Column(db.String(75))
    user_address = db.Column(db.String(75))
    orders = db.relationship('Orders', backref='user',
                            lazy='dynamic')
    def __repr__(self):
        return f"{self.username}" 


class Product(db.Model):
    __tablename__ = 'Product'
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(150))
    product_description = db.Column(db.String(150))
    product_cost = db.Column(db.Numeric(6,2))
    # fk_product_type_id = db.Column(db.Integer, db.ForeignKey('Product_Type.id'))
    def __repr__(self):
        return f"{self.product_name}"    

# class Product_Type(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     product_category = db.Column(db.String(150))
#     def __repr__(self):
#         return f"{self.product_category}"

class Orders(db.Model):
    __tablename__ = 'Orders'
    id = db.Column(db.Integer, primary_key=True)
    order_placed = db.Column(db.DATETIME)
    order_total = db.Column(db.Numeric(7,2))
    orderer = db.Column(db.Integer, db.ForeignKey('user.id'))
    product_ordered = db.Column(db.Integer, db.ForeignKey('Product.id'))
    def __repr__(self):
        return f"{self.order_placed}"
    
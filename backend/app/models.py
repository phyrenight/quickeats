from datatime import datetime
from app import db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), index=True)
    last_name = db.Column(db.String(100), index=True)
    email = db.Column(db.String(250), index=True, unique=True)
    password = db.Column(db.String(250))
    order = db.relationship('Order',
                            backref='customer_id',
                            lazy='dynamic')

class Menu_Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(100), index=True)
    price = db.Column(db.Float)
    description = db.Column(db.String(250))
    img = db.Column(db.String(250)))
    item_in_order = db.relationship('item_in_order',
                                    backref='menu_item_id',
                                    lazy='dynamic')

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    order_date = db.Column(db.String)
    items_in_order = db.relationship('item_in_order',
                                     backref='order_id',
                                     lazy='dynamic')

class Items_in_Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    menu_item_id = db.Column(db.Integer, db.ForeignKey('menu_item.id'))

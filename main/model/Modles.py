from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Customer(db.Model):
    __tablename__ = 'customer'

    c_id = db.Column(db.Integer, primary_key=True)
    c_name = db.Column(db.String(60), nullable=False)
    c_address = db.Column(db.String(60))
    c_email = db.Column(db.String(60), nullable=False)
    c_phone = db.Column(db.String(60))
    e_storeName = db.Column(db.String(250), db.ForeignKey("e_store.name"))
    orders = db.relationship('Order', backref='customer', lazy=True)


class EStore(db.Model):
    __tablename__ = 'e_store'

    name = db.Column(db.String(60), primary_key=True)
    address = db.Column(db.String(60))
    phone_no = db.Column(db.String(60))
    products = db.relationship('Product', backref='e_store', lazy=True)


class Product(db.Model):
    __tablename__ = 'product'

    p_id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(60))
    stock = db.Column(db.String(60))
    price = db.Column(db.Integer)
    size = db.Column(db.String(3))
    color = db.Column(db.String(60))
    p_code = db.Column(db.Integer, primary_key=True)
    e_storeName = db.Column(db.String(250), db.ForeignKey("e_store.name"))


class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    o_date = db.Column(db.Date)
    o_shippingAddress = db.Column(db.String(250))
    o_state = db.Column(db.String(250))
    o_total = db.Column(db.Float)
    o_number = db.Column(db.Integer, nullable=False)
    cusID = db.Column(db.Integer, db.ForeignKey('customer.c_id'), nullable=False)
    proID = db.Column(db.Integer, db.ForeignKey('product.p_id'), nullable=False)

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

    def __init__(self, c_id, c_name, c_address, c_email, c_password, c_phone, e_storeName):
        self.c_id = c_id
        self.c_name = c_name
        self.c_address = c_address
        self.c_email = c_email
        self.c_password = c_password
        self.c_phone = c_phone
        self.e_storeName = e_storeName


class EStore(db.Model):
    __tablename__ = 'e_store'

    name = db.Column(db.String(60), primary_key=True)
    address = db.Column(db.String(60))
    phone_no = db.Column(db.String(60))
    products = db.relationship('Product', backref='e_store', lazy=True)

    def __init__(self, name, address, phone_no):
        self.name = name
        self.address = address
        self.phone_no = phone_no


class Product(db.Model):
    __tablename__ = 'product'

    p_id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(60))
    stock = db.Column(db.String(60))
    price = db.Column(db.Integer)
    size = db.Column(db.String(3))
    color = db.Column(db.String(60))
    p_code = db.Column(db.Integer)
    e_storeName = db.Column(db.String(250), db.ForeignKey("e_store.name"))

    def __init__(self, p_id, category, stock, price, size, color, p_code, e_storeName):
        self.p_id = p_id
        self.category = category
        self.stock = stock
        self.price = price
        self.size = size
        self.color = color
        self.p_code = p_code
        self.e_storeName = e_storeName


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

    def __init__(self, o_date, o_shippingAddress, o_state, o_total, o_number, cusID, proID):
        self.o_date = o_date
        self.o_shippingAddress = o_shippingAddress
        self.o_state = o_state
        self.o_total = o_total
        self.o_number = o_number
        self.cusID = cusID
        self.proID = proID


db.create_all()

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

order_product = db.Table('order_product',
    db.Column('order_id', db.Integer, db.ForeignKey('order.id'), primary_key=True),
    db.Column('product_id', db.Integer, db.ForeignKey('product.id'), primary_key=True)
)


class Customer(db.Model):
    __tablename__ = 'cusomer'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(55))
    address = db.Column(db.String(255))
    email = db.Column(db.String(55))
    password = db.Column(db.String(55))
    phone = db.Column(db.String(55))
    store_name = db.Column(db.String(60), db.ForeignKey("e_store.name"), nullable=False)
    orders = db.relationship('Order', backref='customer', lazy=True)

    def __init__(self, cid, name, address, email, password, phone):
        self.id = cid
        self.name = name
        self.address = address
        self.email = email
        self.password = password
        self.phone = phone


class Product(db.Model):
    __tablename__ = 'product'

    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(255))
    stock = db.Column(db.Integer)
    price = db.Column(db.Double)
    size = db.Column(db.String(5))
    color = db.Column(db.String(55))
    store_name = db.Column(db.String(60), db.ForeignKey("e_store.name"), nullable=False)
    orders = db.relationship('Order', secondary=order_product, backref='products', lazy=True)

    def __init__(self, pid, category, stock, price, size, color):
        self.id = pid
        self.category = category
        self.stock = stock
        self.price = price
        self.size = size
        self.color = color


class Store(db.Model):
    __tablename__ = 'e_store'

    name = db.Column(db.String(60), primary_key=True)
    address = db.Column(db.String(60))
    phone_no = db.Column(db.String(60))
    customers = db.relationship('Customer', backref='customer', lazy=True)
    products = db.relationship('Product', backref='product', lazy=True)

    def __init__(self):
        pass

    def __repr__(self):
        return f'<Store {self.name}>'


class Order(db.Model):
    __tablename__ = 'order'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(20))
    shipping_address = db.Column(db.String(255))
    total = db.Column(db.Integer)
    state = db.Column(db.String(10))
    customer_id = db.Column(db.Integer, db.ForeignKey('cusomer.id'), nullable=False)
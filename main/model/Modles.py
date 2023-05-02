from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class Customer(db.Model):
    __tablename__ = 'cusomer'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(55))
    address = db.Column(db.String(255))
    email = db.Column(db.String(55))
    password = db.Column(db.String(55))
    phone = db.Column(db.String(55))

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

    def __init__(self):
        pass

    def __repr__(self):
        return f'<Store {self.name}>'
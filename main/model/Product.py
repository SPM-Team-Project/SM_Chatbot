from main.Main import db


class Product(db.Model):
    id = db.Column(db.Integer, Primary_key=True)
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

    
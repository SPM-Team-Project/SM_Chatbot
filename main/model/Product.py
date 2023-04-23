from main.main import db


class Product(db.Model):
    id = db.Column(db.Integer, Primary_key=True)
    category = db.Column(db.String(255))
    stock = db.Column(db.Integer)
    price = db.Column(db.Double)
    size = db.Column(db.String(5))
    color = db.Column(db.String(55))

    def __init__(self):
        pass

# TODO: set functions for search, searchById, add, update, and delete
    
from main.main import db


class Product(db.Model):
    id = db.Column(db.Int, )
    category = db.Column(db.String())
    stock = db.Column(db.String())
    price = db.Column(db.String())
    size = db.Column(db.String())
    color = db.Column(db.String())

    def __init__(self):
        pass
    
from main.main import db


class Customer(db.Model):
    id = db.Column(db.Integer, Primary_key=True)
    name = db.Column(db.String(55))
    address = db.Column(db.String(255))
    email = db.Column(db.String(55))
    password = db.Column(db.String(55))
    phone = db.Column(db.String(55))

    def __init__(self):
        pass

# TODO: set functions for search, searchById, add, update, and delete

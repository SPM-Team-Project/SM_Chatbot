from main.main import db


class Customer(db.Model):
    id = db.Column(db.Int, unique=True, nullable=False)
    name = db.Column(db.String(255))
    address = db.Column(db.String(255))
    email = db.Column(db.String(255))
    password = db.Column(db.String(255))
    phone = db.Column(db.String(255))

    def __init__(self):
        pass

from main.main import db


class Store(db.Model):
    name = db.Column(db.String(55), Primary_key=True)
    address = db.Column(db.String(255))
    phone = db.Column(db.String(55))

    def __init__(self):
        pass

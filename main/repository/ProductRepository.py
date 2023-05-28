from main.model.Modles import Product, db


# TODO: think about way to catch if the id is not found in DB
def get_by_id(pid):
    return Product.query.get(pid)


# TODO: for the @param->(pid) it should be auto generated
# TODO: should deal when the product could not added
def add(pid, category, stock, price, size, color):
    new_product = Product(pid, category, stock, price, size, color)
    db.session.add(new_product)

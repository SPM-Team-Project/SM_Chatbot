from main.model.Modles import Customer, db


# TODO: think about way to catch if the id is not found in DB
def get_by_id(cid):
    return Customer.query.get(cid)


# TODO: for the @param->(cid) it should be auto generated
# TODO: should find way to deal when we can not add customer
def add(cid, name, address, email, password, phone):
    new_customer = Customer(cid, name, address, email, password, phone)
    db.session.add(new_customer)


def add_by_object(customer):
    db.session.add(customer)

def update(cid, name, address, email, password, phone):
    customer = get_by_id(cid)
    if name is not None:
        customer.name = name
    if address is not None:
        customer.address = address
    if email is not None:
        customer.email = email
    if password is not None:
        customer.email = email
    if phone is not None:
        customer.phone = phone

# TODO: set functions for delete

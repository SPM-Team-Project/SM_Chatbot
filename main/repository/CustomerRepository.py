from main.model.Modles import Customer, db


# TODO: think about way to catch if the id is not found in DB
def get_by_id(cid):
    return Customer.query.get(cid)


# TODO: for the @param->(cid) it should be auto generated
# TODO: should find way to deal when we can not add customer
def add(name, address, email, phone):
    new_customer = Customer(name, address, email, phone)
    db.session.add(new_customer)
    db.session.commit()
    return new_customer


def add_by_object(customer):
    db.session.add(customer)
    db.session.commit()


def update(cid, name, address, email, password, phone):
    customer = get_by_id(cid)
    if name is not None:
        customer.c_name = name
    if address is not None:
        customer.c_address = address
    if email is not None:
        customer.c_email = email
    if password is not None:
        customer.password = password
    if phone is not None:
        customer.c_phone = phone
    db.session.commit()
# TODO: set functions for delete

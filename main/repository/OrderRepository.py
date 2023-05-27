from main.model.Modles import Order, db
from datetime import datetime
import random


def create_order(shipping_address, customer, product):
    cus_id = customer.c_id
    product_id = product.p_id
    total = product.price

    order = Order(
        o_date=datetime.now().date(),
        o_shippingaddress=shipping_address,
        o_state='ordered',
        o_total=total,
        o_number=random.randint(1, 100000000000),
        cusid=cus_id,
        proid=product_id
    )
    db.session.add(order)
    product.stock = product.stock-1
    db.session.commit()

    return order

from main.model import Modles
import random


def get_three_random_products():
    all_products = Modles.Product.query.all()
    random_products = random.sample(all_products, 3)
    product_list = []
    for index, product in enumerate(random_products, start=1):
        product_data = {
            f'p{index}': {
                'category': product.category,
                'price': product.price,
                'size': product.size,
                'color': product.color
            }
        }
        product_list.append(product_data)
    return product_list


def get_product_by_code(code):
    query_result = Modles.Product.query.filter_by(p_code=code).first()
    if query_result is not None:
        product = {
            'category': query_result.category,
            'stock': query_result.stock,
            'price': query_result.price,
            'size': query_result.size,
            'code': query_result.p_code,
            'color': query_result.color
        }
        return product
    else:
        return {'error': 'Product not found'}

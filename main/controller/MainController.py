from flask import jsonify
from main.main import app
from main.model import Modles
import random


@app.route('/api', methods=['GET'])
def api():
    data = {
        'message': 'Hello, World!'
    }
    return jsonify(data)


@app.route('/marketChatbot/api/v1/randomProduct', methods=['GET'])
def random_products():
    products = get_three_random_products()
    return jsonify(products)


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
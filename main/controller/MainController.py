from flask import jsonify
from main.main import app


@app.route('/api', methods=['GET'])
def api():
    data = {
        'message': 'Hello, World!'
    }
    return jsonify(data)

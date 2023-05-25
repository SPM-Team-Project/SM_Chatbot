from flask import request, jsonify
from run import app


@app.route('/api', methods=['GET'])
def api():
    data = {
        'message': 'Hello, World!'
    }
    return jsonify(data)



from flask import request
from main.Main import app
from main.model import Modles


@app.route("/chop/api/v1/message", methods=['POST'])
def receive_message():
    message = request.get_json()  # Extract the message from the request JSON

    print("Received message:", message)  # Print the message

    return {"success": True}  # Return a response indicating success


@app.route("/chop/api/v1/randomProduct",methods=['POST'])
def random_product():
    message = request.get_json()


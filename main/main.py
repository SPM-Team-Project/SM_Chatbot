from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# TODO: make the app config to connect it to database
app = Flask(__name__)
db = SQLAlchemy(app)

db.create_all()


@app.route('/')
def index():
    return ""


if __name__ == '__main__':
    app.run()

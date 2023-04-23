from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

db.create_all()


@app.route('/')
def index():
    return ""


if __name__ == '__main__':
    app.run()

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# TODO: make the app config to connect it to database
app = Flask(__name__)

# adding configuration for using a sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)
db.create_all()

@app.route('/')
def index():
    return ""


if __name__ == '__main__':
    app.run()

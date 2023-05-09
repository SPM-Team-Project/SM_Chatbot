from flask import Flask
from model.Modles import db
from model.Modles import Store

app = Flask(__name__)


# adding configuration for using a sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/product'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.route('/')
def index():
    try:
        s = Store.query.filter_by(name='ss').first()
        return s.name
    except Exception as e:
        return f"An error occurred: {str(e)}"


if __name__ == '__main__':
    app.run()

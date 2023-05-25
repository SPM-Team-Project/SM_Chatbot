from flask import Flask
from main.model.Modles import db
from main.model.Modles import Store
import os


def create_app():
    app = Flask(__name__)
    # set DATABASE_URL=postgresql://smchatbotdatabase_user:YLSGBHn1SnRKmRKRpiY2ZImMjdb0CciZ@dpg-chn735vdvk4n43a6131g-a.oregon-postgres.render.com/smchatbotdatabase
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    return app


app = create_app()


@app.route('/', methods=['GET'])
def main():
    return "hi welcome :)"


@app.route('/test', methods=['GET'])
def test():
    print("it is work at lest")
    try:
        s = Store.query.filter_by(name='ss').first()
        return s.name
    except Exception as e:
        return f"An error occurred: {str(e)}"


if __name__ == '__main__':
    # Create the database tables
    app = create_app()
    with app.app_context():
        db.create_all()

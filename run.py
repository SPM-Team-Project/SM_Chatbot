from main.main import app
from main.model.Modles import db

if __name__ == '__main__':
    with app.app_context():
        db.init_app(app)
        db.create_all()
    app.run()

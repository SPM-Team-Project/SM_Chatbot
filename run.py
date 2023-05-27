from main.main import app
from main.model.Modles import db

if __name__ == '__main__':
    app.run()
    db.create_all()

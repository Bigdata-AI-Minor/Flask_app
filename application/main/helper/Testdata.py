from application.main import db
from application.main.model import User
from application.main.model.enums.User_roll import User_roll
from application.main.model.User import User
import flask_bcrypt

class Testdata():
    # populate db with users
    @staticmethod
    def populate_database():
        # hashed_password = flask_bcrypt.generate_password_hash('test').decode('utf-8')
        try:
            admin_user = User(Username='test', Password='test', Role=User_roll.ADMIN.value)
            db.session.add(admin_user)
            db.session.commit()
        except:
            None
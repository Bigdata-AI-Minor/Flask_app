from .. import db,flask_bcrypt


class User(db.Model):
    __tablename__="User"

    Id=db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    Username=db.Column(db.String(50), unique=True)
    Password=db.Column(db.String(100), nullable=False)
    Role=db.Column(db.Integer, nullable=False)
    _current_user = None

    def __init__(self, Username, Password, Role):
        self.Username = Username
        self.password = Password
        self.Role = Role
    
    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        self.Password = flask_bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password: str) -> bool:
        return flask_bcrypt.check_password_hash(self.Password, password)
    
    # check the password requirments
    def is_valid_password(password: str) -> bool:
        if len(password) >= 8:
            l = sum(1 for i in password if i.islower())
            u = sum(1 for i in password if i.isupper())
            d = sum(1 for i in password if i.isdigit())
            p = sum(1 for i in password if i in "$@_!")
            return l >= 1 and u >= 1 and p >= 1 and d >= 1 and (l + p + u + d) == len(password)
        return False
    
    @staticmethod
    def get_current_user():
        return User._current_user
    
    @staticmethod
    def set_current_user(user):
        User._current_user = user


  
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
       return all([
        len(password) >= 8,
        any(char.isdigit() for char in password),
        any(char.isupper() for char in password),
        any(char.islower() for char in password),
        any(char in "!@#$%^&*()-_=+[]{};:,.<>/?`~\\" for char in password)
    ])
    
    @staticmethod
    def get_current_user():
        return User._current_user
    
    @staticmethod
    def set_current_user(user):
        User._current_user = user


  
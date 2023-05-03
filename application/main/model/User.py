from .. import db,flask_bcrypt


class User(db.Model):
    __tablename__="User"

    Id=db.Column(db.Integer, primary_key=True, unique=True,autoincrement=True)
    Username=db.Column(db.String(50), unique=True)
    Password=db.Column(db.String(100), nullable=False)
    Role=db.Column(db.Integer, nullable=False)
    # Jwt_token=db.Column(db.String(50), unique=True)

    
    @property
    def Password(self):
        raise AttributeError('password: write-only field')

    @Password.setter
    def Password(self, password):
        self.Password = flask_bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password: str) -> bool:
        return flask_bcrypt.check_password_hash(self.password_hash, password)


  
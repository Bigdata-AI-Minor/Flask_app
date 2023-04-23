from ...main import db

class User_repo(db.Model):
    __tablename__="User"

    Id=db.Column(db.Integer, primary_key=True, unique=True)
    Name=db.Column(db.String(50), unique=True)
    Password=db.Column(db.String(100), nullable=False)
    Role=db.Column(db.Integer, nullable=False)
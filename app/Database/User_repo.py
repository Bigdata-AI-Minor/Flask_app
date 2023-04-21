from .. import db

class User_repo(db.Model):
    __tablename__ = "User"

    id = db.Column(db.Integer, primary_key = True, unique = True)
    name = db.Column(db.String(50), unique = True)
    password = db.Column(db.String(100), nullable = False)
    role = db.Column(db.Integer, nullable = False)


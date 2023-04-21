from .. import db

class User_repo(db.Model):
    __tablename__ = "jwt"

    id = db.Column(db.String, primary_key=True, unique = True)
    user_id = db.Column(db.Integer, nullable = False)
    jwt = db.Column(db.String(100), nullable = False)
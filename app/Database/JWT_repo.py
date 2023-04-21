from .. import db

class Jwt_repo(db.Model):
    __tablename__ = "Jwt"

    id = db.Column(db.Integer, primary_key=True, unique = True)
    user_id = db.Column(db.Integer, nullable = False)
    jwt = db.Column(db.String(100), nullable = False)
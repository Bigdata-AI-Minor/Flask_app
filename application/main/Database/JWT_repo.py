from ... import db

class Jwt_repo(db.Model):
    __tablename__="Jwt"

    Id=db.Column(db.Integer, primary_key=True, unique=True)
    User_id=db.Column(db.Integer, nullable=False)
    Jwt=db.Column(db.String(100), nullable=False)
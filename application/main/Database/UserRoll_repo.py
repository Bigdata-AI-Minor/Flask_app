from ...main import db

class User_roll_repo(db.Model):
    __tablename__="UserRoll"

    Id=db.Column(db.Integer, primary_key=True, unique=True)
    Roll=db.Column(db.String(100), nullable=False)
from app import db

class Class_repo(db.Model):
    __tablename__ = "UserRoll"

    id = db.Column(db.Integer, primary_key = True, unique = True)
    Roll = db.Column(db.String(100), nullable = False)
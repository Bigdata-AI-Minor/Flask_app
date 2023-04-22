from app import db

class Class_repo(db.Model):
    __tablename__ = "Classification"

    id = db.Column(db.Integer, primary_key = True, unique = True)
    classification = db.Column(db.String(100), nullable = False)
from app import db

class Class_repo(db.Model):
    __tablename__ = "Classification"

    id = db.Column(db.String, primary_key = True, unique = True)
    classification = db.Column(db.Integer, nullable = False)
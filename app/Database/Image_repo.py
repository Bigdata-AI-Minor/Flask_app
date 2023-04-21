from app import db
import datetime

class User_repo(db.Model):
    __tablename__ = "Image"

    id = db.Column(db.Integer, primary_key = True, unique = True)
    classification = db.Column(db.Integer, nullable = False)
    long = db.Column(db.Float, nullable = False)
    lan = db.Column(db.Float, nullable = False)
    created = db.Column(db.String, nullable = False)
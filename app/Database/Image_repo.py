from .. import db
import datetime

class User_repo(db.Model):
    __tablename__ = "image"

    id = db.Column(db.String, primary_key = True, unique = True)
    classification = db.Column(db.Integer, nullable = False)
    long = db.Column(db.Float, nullable = False)
    lan = db.Column(db.Float, nullable = False)
    created = db.Column(db.String, nullable = False)
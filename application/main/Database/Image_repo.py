from ...main import db
import datetime

class User_repo(db.Model):
    __tablename__="Image"

    Id=db.Column(db.Integer, primary_key=True, unique=True)
    Classification=db.Column(db.Integer, nullable=False)
    Long=db.Column(db.Float, nullable=False)
    Lan=db.Column(db.Float, nullable=False)
    Created=db.Column(db.String(255), nullable=False)
    BitString=db.Column(db.String, nullable=False)
from .. import db

class Classification(db.Model):
    __tablename__="Classification"


    id = db.Column(db.Integer, primary_key=True, unique=True , autoincrement=True, nullable=False)
    classification = db.Column(db.String(100), nullable=False, unique=True)


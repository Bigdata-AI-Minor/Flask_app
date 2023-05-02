from .. import db

class Image(db.Model):
    __tablename__="Image"

    id=db.Column(db.Integer, primary_key=True, unique=True)
    classification=db.Column(db.Integer, nullable=False)
    # classification = db.relationship('Classification', backref=db.backref('images', lazy=True))
    long=db.Column(db.Float, nullable=False)
    lan=db.Column(db.Float, nullable=False)
    created=db.Column(db.String(255), nullable=False)
    bit_string=db.Column(db.String, nullable=False)


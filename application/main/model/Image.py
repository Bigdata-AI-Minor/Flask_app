from .. import db

class Image(db.Model):
    __tablename__="Image"

    id=db.Column(db.Integer, primary_key=True, unique=True)
    image_bit_string_id = db.Column(db.Integer, db.ForeignKey('Image_bit_string.id'), unique=True)
    classification=db.Column(db.Integer, nullable=False)
    long=db.Column(db.Float, nullable=False)
    lan=db.Column(db.Float, nullable=False)
    created=db.Column(db.String(255), nullable=False)


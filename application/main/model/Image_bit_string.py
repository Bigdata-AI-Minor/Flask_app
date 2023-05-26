from .. import db

class Image_bit_string(db.Model):
    __tablename__="Image_bit_string"

    id=db.Column(db.Integer, primary_key=True, unique=True)
    bit_string=db.Column(db.String, nullable=False)
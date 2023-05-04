import base64
import imghdr

from flask import request
from ..model.Image import Image
from ..model.Image import db
from application.main.model.Image import Image
from application.main.model.Classification import Classification
from application.main.service.Classification_service import Classification_service
from typing import Dict, Tuple

class Image_service():

    def __init__(self) -> None:
        pass

    def Create_image(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
        bit_string = data['bit_string']
        classification = data['classification']
        long = data['long']
        lan = data['lan']
        created = data['created']

        try:
            image = Image.query.filter_by(bit_string=bit_string).first_or_404()
        except:
            image = None

        if image:
            response_object = {
                'status': 'fail',
                'message': 'Image already exists',
            }
            return response_object, 409


        classification_names = [classification.classification for classification in Classification_service.get_classifications()]
        if classification not in classification_names:
            response_object = {
                'status': 'fail',
                'message': 'Classification does not exist',
            }
            return response_object, 409

        if not Image_service.is_base64_image(bit_string):
            response_object = {
                'status': 'fail',
                'message': 'bit_string is not a base64 image',
            }
            return response_object, 409
        

        image = Image(classification=classification, long=long, lan=lan, 
                                  created=created, bit_string=bit_string)
        
        return Image_service.save_changes(image, "successfully uploaded an image to the database")

    def Delete_image(id: str):

        image = Image.query.filter_by(id=id).first_or_404()
        if request.method == 'DELETE':
            db.session.delete(image)
            db.session.commit()
        #db.session.delete(Image.query.filter_by(id=id).first())

        response_object = {
        'status': 'success',
        'message': 'Successfully deleted a image.',
        }
        return response_object, 201

    def Edit_image(id:  str, classification: int):
        # TODO edit classification
        if id:
            image = Image.query.filter_by(id=id).first_or_404()
            image.classification = classification
            db.session.commit()

        response_object = {
        'status': 'success',
        'message': 'Successfully updated the image.',
        }
        return response_object, 201

    def get_image(id: str):
        # return None
        if id:
            return Image.query.filter_by(id=id).first_or_404()
        return Image.query.all()

    def save_changes(data: Image, message) -> Tuple[Dict[str, str], int]:
        db.session.add(data)
        db.session.commit()

        response_object = {
            'status': 'success',
            'message': message,
        }
        return response_object, 201

    def is_base64_image(s):
        try:
            decoded_data = base64.b64decode(s)
            if imghdr.what(None, decoded_data) is not None:
                return True
            else:
                return False
        except:
            return False
    
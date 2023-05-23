import base64
import imghdr
from datetime import datetime
from flask import request

from application.main.responses.images.Image_Response import Image_Response
from ..model.Image import Image
from ..model.Image import db
from application.main.model.Image import Image
from application.main.model.Image_bit_string import Image_bit_string

from application.main.service.Classification_service import Classification_service
from typing import Dict, Tuple

class Image_service():

    def __init__(self) -> None:
        pass

    def Create_image(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
        classification = data['classification']
        long = data['long']
        lan = data['lan']
        created = data['created']
        image_bit_string_id = data['image_bit_string_id']

        try:
            image = Image.query.filter_by(image_bit_string_id=image_bit_string_id).first_or_404()
        except:
            image = None

        if image:
            response_object = {
                'status': 'fail',
                'message': 'Image already exists',
            }
            return response_object, 409
        
        try:
            image_bit_string = Image_bit_string.query.filter_by(id=image_bit_string_id).first_or_404()
        except:
            image_bit_string = None
        
        if not image_bit_string:
            response_object = {
                'status': 'fail',
                'message': 'Image bit string does not exist',
            }
            return response_object, 409

        classification_ids = [classification.id for classification in Classification_service.get_classifications()]
        if classification not in classification_ids:
            response_object = {
                'status': 'fail',
                'message': 'Classification does not exist',
            }
            return response_object, 409
        
        # TODO: what should be the correct date format?
        # if Image_service.is_valid_date(created, "%Y-%m-%d %H:%M:%S") == False:
        #     response_object = {
        #         'status': 'fail',
        #         'message': 'Date time not in correct format, use Y-m-d H:M:S',
        #     }
        #     return response_object, 409

        image = Image(classification=classification, long=long, lan=lan, 
                                  created=created, image_bit_string_id=image_bit_string_id)
        
        return Image_service.save_changes(image, "Successfully uploaded an image to the database")
    

    def Create_image_bit_string(data: str) -> Tuple[Dict[str, str], int]:
        try:
            image = Image_bit_string.query.filter_by(bit_string=data).first_or_404()
        except:
            image = None

        if image:
            response_object = {
                'status': 'fail',
                'message': 'Image bit string already exists',
            }
            return response_object, 409
        
        if not Image_service.is_base64_image(data):
            response_object = {
                'status': 'fail',
                'message': 'bit_string is not a base64 image',
            }
            return response_object, 409
        
        image_bit_string = Image_bit_string(bit_string=data)
        return Image_service.save_changes(image_bit_string, "successfully uploaded an image bit string to the database")

    def Delete_image(id: str):
        try:
            image = Image.query.filter_by(id=id).first_or_404()
            if request.method == 'DELETE':
                db.session.delete(image)
                db.session.commit()
        except:
            response_object = Image_Response('failed', 'internal server error')
            return response_object.image_response(500)
        
        response_object = Image_Response('success', 'Successfully deleted a image.')
        return response_object.image_response(200)

    def Edit_image(id:  int, classification: int):
        if id:
            try:
                image = Image.query.filter_by(id=id).first_or_404()
                image.classification = classification
                db.session.commit()
            except:
                response_object = Image_Response('failed', 'internal server error')
                return response_object.image_response(500)

        response_object = Image_Response('success', 'Successfully edited a image.')
        return response_object.image_response(200)

    def get_image(id: int):
        try:
            return Image.query.filter_by(id=id).first_or_404()
        except:
            response_object = {
            'status': 'failed',
            'message': 'no image with this id',
            }
            return response_object, 404
            
    def get_images():
        try: 
            return Image.query.all()
        except:
            response_object = {
            'status': 'failed',
            'message': 'internal server error',
            }
            return response_object, 500
        
    def get_image_bit_string(id: int):
        try:
            return Image_bit_string.query.filter_by(id=id).first_or_404()
        except:
            response_object = {
            'status': 'failed',
            'message': 'no image with this id',
            }
            return response_object, 404
        
    def get_image_bit_strings():
        try: 
            return Image_bit_string.query.all()
        except:
            response_object = {
            'status': 'failed',
            'message': 'internal server error',
            }
            return response_object, 500

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
        
    def is_valid_date(date_string, date_format):
        try:
            datetime.strptime(date_string, date_format)
            return True
        except ValueError:
            return False
    
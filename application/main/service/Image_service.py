import base64
import imghdr
from datetime import datetime
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
        image_bit_string = Image_bit_string.query.filter_by(id=image_bit_string_id).first()
        imageExists = Image.query.filter_by(image_bit_string_id=image_bit_string_id).first()
        classification_ids = [classification.id for classification in Classification_service.get_classifications()]
        

        if Image_service.is_valid_date(created, "%Y-%m-%d %H:%M:%S") == False:
            response_object = Image_Response('fail', 'Date time not in correct format, use Y-m-d H:M:S')
            return response_object.image_response(409)
        
        if imageExists:
            response_object = Image_Response('fail', 'Image already exists')
            return response_object.image_response(409)
        
        if image_bit_string == None:
            response_object = Image_Response('fail', 'Image bit string does not exist')
            return response_object.image_response(409)
        
        if classification not in classification_ids:
            response_object = Image_Response('fail', 'Classification does not exist')
            return response_object.image_response(409)
        
        else:
            image = Image(classification=classification, long=long, lan=lan, 
                                  created=created, image_bit_string_id=image_bit_string_id)
            db.session.add(image)
            db.session.commit()
            response_object = Image_Response('succes', 'Successfully uploaded an image to the database')
            return response_object.image_response(409)

    def Create_image_bit_string(data: str) -> Tuple[Dict[str, str], int]:
        try:
            if not Image_service.is_base64_image(data):
                response_object = Image_Response('fail', 'bit_string is not a base64 image')
                return response_object.image_response(409)
            image_bit_string = Image_bit_string(bit_string=data)
            db.session.add(image_bit_string)
            db.session.commit()
            response_object = Image_Response('succes', 'Successfully uploaded an image bit string to the database"')
            return response_object.image_response(201)
        except:
            response_object = Image_Response('fail', 'mage bit string already exists')
            return response_object.image_response(409)

        

    def Delete_image(id: str):
        try:
            image = Image.query.filter_by(id=id)
            db.session.delete(image)
            db.session.commit()
            response_object = Image_Response('success', 'Successfully deleted a image.')
            return response_object.image_response(200)
        except:
            response_object = Image_Response('failed', 'internal server error')
            return response_object.image_response(500)
        


    def Edit_image(id:  int, classification: int):
        try:
            image = Image.query.filter_by(id=id)
            image.classification = classification
            db.session.commit()
            response_object = Image_Response('success', 'Successfully edited a image.')
            return response_object.image_response(200)
        except:
            response_object = Image_Response('failed', 'internal server error')
            return response_object.image_response(500)

        

    def get_image(id: int):
        try:
            return Image.query.filter_by(id=id)
        except:
            response_object = Image_Response('failed', 'image id not found')
            return response_object.image_response(404)
            
    def get_images():
        try: 
            return Image.query.all()
        except:
            response_object = Image_Response('failed', 'internal server error')
            return response_object.image_response(500)
        
    def get_image_bit_string(id: int):
        try:
            return Image_bit_string.query.filter_by(id=id)
        except:
            response_object = Image_Response('failed', 'image bit string not found')
            return response_object.image_response(404)
        
    def get_image_bit_strings():
        try: 
            return Image_bit_string.query.all()
        except:
            response_object = Image_Response('failed', 'internal server error')
            return response_object.image_response(500)

    def is_base64_image(s):
        decoded_data = base64.b64decode(s)
        return bool(imghdr.what(None, decoded_data) is not None)
        
    def is_valid_date(date_string, date_format):
        return bool(datetime.strptime(date_string, date_format))
            
    
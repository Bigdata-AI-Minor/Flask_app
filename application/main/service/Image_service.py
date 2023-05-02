from ..model.Image import Image
from ..model.Image import db
from application.main.model.Image import Image
from application.main.model.Classification import Classification

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

        # TODO get all classifications and check if the classification is in the list
        # if not return error

        # TODO check if the bit_string is a valid 64 bit string
        # TODO classifiation object forceren

        if image:
            response_object = {
                'status': 'fail',
                'message': 'Image already exists',
            }
            return response_object, 409
        
        image = Image(classification=classification, long=long, lan=lan, 
                                  created=created, bit_string=bit_string)
        
        return Image_service.save_changes(image, "successfully uploaded an image to the database")

    def Delete_image(id: str):
        return ""

    def Edit_image(id:  str, image: Image):
        return ""

    def get_image(id: str):
        return None
        if id:
            images = Image.query.filter_by(id=id).first_or_404()
        images =  Image.query.all()
        image_dicts = [image.__dict__ for image in images]
        return image_dicts

    def save_changes(data: Image, message) -> Tuple[Dict[str, str], int]:
        db.session.add(data)
        db.session.commit()

        response_object = {
            'status': 'success',
            'message': message,
        }
        return response_object, 201
    
from ..model.Image import Image
from ..Database.Image_repo import db
from ..Database import Image_repo
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

        if Image_repo.query.filter_by(bit_string=bit_string).first():
            response_object = {
                'status': 'fail',
                'message': 'Image already exists',
            }
            return response_object, 409
        
        image = Image_repo(classification=classification, long=long, lan=lan, 
                                  created=created, bitString=bit_string)
        
        return Image_service.save_changes(image)

    def Delete_image(id: str):
        return ""
    
    def Edit_image(id:  str, image: Image):
        return ""

    def get_image(id: str):
        return ""
    
    def get_images():
        return Image_repo.query.all()
        # return None

        
    def save_changes(data: Image_repo) -> Tuple[Dict[str, str], int]:
        db.session.add(data)
        db.session.commit()

        response_object = {
            'status': 'success',
            'message': 'Successfully registered.',
        }
        return response_object, 201
    
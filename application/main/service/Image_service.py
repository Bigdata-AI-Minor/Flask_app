from ..model.Image import Image
from ..Database.Image_repo import db
from application.main.Database.Image_repo import Image_repo
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
            image = Image_repo.query.filter_by(bit_string=bit_string).first_or_404()
        except:
            image = None

        if image:
            response_object = {
                'status': 'fail',
                'message': 'Image already exists',
            }
            return response_object, 409
        
        image = Image_repo(classification=classification, long=long, lan=lan, 
                                  created=created, bit_string=bit_string)
        
        return Image_service.save_changes(image, "uccessfully uploaded an image to the atabase")

    def Delete_image(id: str):
        return ""
    
    def Edit_image(id:  str, image: Image):
        return ""

    def get_image(id: str):
        return ""
    
    def get_images():
        return Image_repo.query.all()
        # return None

        
    def save_changes(data: Image_repo, message) -> Tuple[Dict[str, str], int]:
        db.session.add(data)
        db.session.commit()

        response_object = {
            'status': 'success',
            'message': message,
        }
        return response_object, 201
    
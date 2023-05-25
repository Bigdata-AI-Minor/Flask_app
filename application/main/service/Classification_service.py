from application.main.responses.images.Image_Response import Image_Response
from ..model.Classification import db
from application.main.model.Classification import Classification

from typing import Dict, Tuple

class Classification_service():

    def __init__(self) -> None:
        pass

    def create_classification(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
        options = ['plastic', 'metal', 'cardboard', 'other']
        classification = data['classification']
        if classification not in options:
            response_object = Image_Response('fail', 'classification not in list of options')
            return response_object.image_response(409)
        try:
            classification_obj = Classification.query.filter_by(classification=classification).first_or_404()
            classification_obj = Classification(classification=classification)
            db.session.add(classification_obj)
            db.session.commit()

            response_object = Image_Response('success', 'Successfully uploaded an image to the database')
            return response_object.image_response(201)
        except:
            response_object = Image_Response('conflict', 'classification already exists')
            return response_object.image_response(409)
        
        
    
    def get_classifications():
        return Classification.query.all()
    
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
            response_object = {
                'status': 'fail',
                'message': 'classification not in list of options',
            }
            return response_object, 409

        try:
            classification_obj = Classification.query.filter_by(classification=classification).first_or_404()
        except:
            classification_obj = None

        if classification_obj:
            response_object = {
                'status': 'fail',
                'message': 'classification already exists',
            }
            return response_object, 409
        
        classification_obj = Classification(classification=classification)
        
        return Classification_service.save_changes(classification_obj, "successfully uploaded an classification to the database")

    def get_classifications():
        return Classification.query.all()

    def save_changes(data: Classification, message) -> Tuple[Dict[str, str], int]:
        db.session.add(data)
        db.session.commit()

        response_object = {
            'status': 'success',
            'message': message,
        }
        return response_object, 201
    
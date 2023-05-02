from ..model.Classification import db
from application.main.model.Classification import Classification

from typing import Dict, Tuple

class Classification_service():

    def __init__(self) -> None:
        pass

    def create_classification(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
        return None


    def get_classifications(id: str):
        return None

    def save_changes(data: Classification, message) -> Tuple[Dict[str, str], int]:
        db.session.add(data)
        db.session.commit()

        response_object = {
            'status': 'success',
            'message': message,
        }
        return response_object, 201
    
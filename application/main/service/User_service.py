from ..model.User import User
from..service.JWT_service import JWT_service
from ..model.User import db
from typing import Dict, Tuple
import uuid
import datetime

class User_service():

    def create_user(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
        user = User.query.filter_by(Username=data['Username']).first()
     
        if not user:
            new_user = User(
                Username=data['Username'],
                Password=data['Password'],
                Role=data['Role']
            )
            db.session.add(new_user)
            db.session.commit()
            return JWT_service.generate_JWT_token(new_user)
        else:
            response_object = {
                'status': 'fail',
                'message': 'User already exists. Please Log in.',
            }

        return response_object, 409  

    def delete_user(id: str):
        return ""
    
    def edit_user(id:  str, image: User):
        return ""

    def get_user_by_id(id: str):
        try:
            return User.query.filter_by(name=db.get('Id')).first()
        except Exception as exception:
            return exception
    
    def get_user_by_name(id: str):
        try:
            return User.query.filter_by(name=db.get('username')).first()
        except Exception as exception:
            return exception
    
    def get_users():
        try:
            return User.query.all()
        except Exception as exception:
            return exception

        
    
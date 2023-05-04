from ..model.User import User
from..service.JWT_service import JWT_service
from ..model.User import db
from typing import Dict, Tuple, Any
from ..responses.user.User_Reponse import User_Response


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
            response_object = User_Response('fail','User already exists. Please Log in.')
        return response_object.user_response(409) 

    def delete_user_by_id(id: int):
        try:
            user = User.query.filter_by(Id=id).first()
            db.session.delete(user)
            db.session.commit()
            response_object = User_Response('success','Successfully deleted a user')
            return response_object.user_response(201)
        except Exception as exception:
            response_object = User_Response('fail', f'User id does not exist: {exception}')
            return response_object.user_response(409)
        
    def edit_user_by_Id(id: int, data: Dict[str, Any]):
        user = User.query.filter_by(Id=id).first()
        print(data)
        if user:
            user.Username=data['Username']
            user.Password=data['Password']
            user.Role=data['Role']
            db.session.commit()
        
        response_object = User_Response('success','Successfully updated a user')
        return response_object.user_response(201)


    def get_user_by_id(id: int):
        try:
            return User.query.filter_by(Id=id).first()
        except Exception as exception:
            response_object = User_Response('fail', f'Something went wrong {exception}')
            return response_object.user_response(409)  
    
    
    def get_users():
        try:
            return User.query.all()
        except Exception as exception:
            response_object = User_Response('fail', f'Something went wrong {exception}')
            return response_object.user_response(409)

        
    
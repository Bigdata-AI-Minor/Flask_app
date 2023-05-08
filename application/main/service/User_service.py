from ..model.User import User
from..service.JWT_service import JWT_service
from ..model.User import db
from typing import Dict, Tuple, Any
from ..responses.user.User_Reponse import User_Response
from ..model.enums.User_roll import User_roll
# from ..helper.auth_helper import Auth_Helper
from ..service.Auth_service import Auth_service


class User_service():
    def create_user(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
        user = User.query.filter_by(Username=data['Username']).first()

        # TODO test the function if it checks if the entered password is valid
        # if not User.is_valid_password(data['Password']):
        #     response_object = User_Response('fail','Entered password is not valid')
        #     return response_object.user_response(409) 
        
        if not user:
            new_user = User(
                Username=data['Username'],
                Password=data['Password'],
                Role=User_roll.VOLUNTEER.value
            )
            db.session.add(new_user)
            db.session.commit()
            return JWT_service.generate_JWT_token(new_user)
        else:
            response_object = User_Response('fail',f'User {new_user.Username} already exists. Please Log in.')
        return response_object.user_response(409) 

    def delete_user_by_id(id: int):
        try:
            user = User.query.filter_by(Id=id).first()
            db.session.delete(user)
            db.session.commit()
            response_object = User_Response('success',f'Successfully deleted user {user.Username}')
            return response_object.user_response(200)
        except Exception as exception:
            response_object = User_Response('fail', f'User id:{id} does not exist')
            return response_object.user_response(409)
    
    # TODO check the user rights and save the input based on that
    def edit_user_by_Id(id: int, data: Dict[str, Any]):
        user = User.query.filter_by(Id=id).first()
        current_user = User.get_current_user()
        if user:
            if current_user.Role != User_roll.ADMIN.value:
                user.Password=data['Password']
            else:
                user.Username=data['Username']
                user.Password=data['Password']
                user.Role=data['Role']
            db.session.commit()
        response_object = User_Response('success',f'Successfully updated user {user.Username}')
        return response_object.user_response(200)

    def get_user_by_id(id: int):
        try:
            return User.query.filter_by(Id=id).first()
        except Exception as exception:
            response_object = User_Response('fail', f'id:{id} does not exist')
            return response_object.user_response(409)  
    
    def get_users():
        try:
            return User.query.all()
        except Exception as exception:
            response_object = User_Response('fail', f'Internal server error: {exception}')
            return response_object.user_response(500)

        
    
from ..model.JWT import Jwt
from ..model.JWT import db
from ..model.User import User
from typing import Dict, Tuple
from ..config import key
import datetime
from ..responses.user.User_Reponse import User_Response

class JWT_service():

    # create a JWT token
    @staticmethod
    def encode_JWT_token(user_id: int)-> bytes:
        try:
            payload = {'expire': datetime.datetime.utcnow() + datetime.timedelta(days=30),
                       'issued': datetime.datetime.utcnow(),
                       'subject': user_id}
        except Exception as exception:
            return exception
        return Jwt.encode(payload, key,algorithm='HS256')

    # validate the JWT token
    @staticmethod
    def validate_JWT(token: Jwt,secret):
        try:
            payload = Jwt.decode(token, secret, algorithms=["HS256"])
        except Exception:
            return "invalid token"
        return payload
    
    def generate_JWT_token(user: User) -> Tuple[Dict[str, str], int]:
        try:
            auth_token = JWT_service.encode_JWT_token(user.id)
            response_object = {
            'status': 'success',
            'message': 'Successfully registered.',
            'Authorization': auth_token.decode()
            }
            return response_object, 201
        except Exception as exception:
            response_object = User_Response('fail',f'Some error occurred. Please try again.:{exception}')
        return response_object.user_response(401)
        




from ..model.User import User
from typing import Dict, Tuple
from ..config import key
import datetime
from ..responses.user.User_Reponse import User_Response
from ..responses.auth.JWTtokenResponse import JWTtokenResponse
import jwt

class JWT_service():

    # create a JWT token, valid for 30 days
    @staticmethod
    def encode_JWT_token(user_id: int)-> bytes:
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=30),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id
            }
            return jwt.encode(payload,key,algorithm='HS256')
        except Exception as exception:
            response_object = User_Response('fail',f'Some error occurred. Please try again.:{exception}')
            return response_object.user_response(401)

    # validate the jwt_ token
    @staticmethod
    def validate_JWT(token: jwt,secret):
        try:
            payload = jwt.decode(token, secret, algorithms=["HS256"])
        except Exception as exception:
            response_object = User_Response('fail',f'invalid token. :: {exception}')
            return response_object.user_response(401)
        return payload
    
    # generate jwt_token
    def generate_JWT_token(user: User) -> Tuple[Dict[str, str], int]:
        try:
            auth_token = JWT_service.encode_JWT_token(user.Id)
            response_object = JWTtokenResponse('success','Successfully registered',auth_token.decode())
            return response_object.auth_response(201)
        except Exception as exception:
            response_object = User_Response('fail',f'Some error occurred. Please try again.:{exception}')
        return response_object.user_response(401)
        




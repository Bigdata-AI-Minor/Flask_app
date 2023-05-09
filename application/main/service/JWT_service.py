from ..model.User import User
from typing import Dict, Tuple
from ..config import key
import datetime
from ..responses.user.User_Reponse import User_Response
from ..responses.auth.JWTtokenResponse import JWTtokenResponse
from ..service.BlacklistJwt_service import BlacklistJwtToken
import jwt

class JWT_service():

    # create a JWT token, valid for 30 days
    @staticmethod
    def encode_JWT_token(Id: int)-> bytes:
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=30),
                'iat': datetime.datetime.utcnow(),
                'sub': Id
            }
            return jwt.encode(payload,key,algorithm='HS256')
        except Exception as exception:
            response_object = JWTtokenResponse('fail',f'Some error occurred. Please try again.')
            return response_object.auth_response(401)

    # validate and decode the jwt_ token
    @staticmethod
    def validate_JWT(token: jwt):
        try:
            payload = jwt.decode(token, key, algorithms=["HS256"])
            if(BlacklistJwtToken.check_blacklist(token)):
                return JWTtokenResponse('fail','token has been blacklisted.')
            return payload['sub']
        except jwt.ExpiredSignature:
            response_object = JWTtokenResponse('fail','token has been expired.')
            return response_object.auth_response(401)
        except jwt.InvalidTokenError:
            response_object = JWTtokenResponse('fail','invalid token.')
            return response_object.auth_response(401)
      
    # generate jwt_token
    def generate_JWT_token(user: User) -> Tuple[Dict[str, str], int]:
        try:
            auth_token = JWT_service.encode_JWT_token(user.Id)
            response_object = JWTtokenResponse('success','Successfully registered',auth_token.decode())
            return response_object.jwt_auth_response(201)
        except Exception:
            response_object = User_Response('fail',f'Some error occurred. Please try again')
        return response_object.user_response(401)
        




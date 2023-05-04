from ..model.JWT import db
from typing import Dict, Tuple
from ..model.User import User
from ..service.User_service import User_service
from ..service.JWT_service import JWT_service
from ..responses.auth.JWTtokenResponse import JWTtokenResponse, JWTtokenResponseEncoder
import json

class Auth_service():

    def login(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
        try:
            user = User.query.filter_by(Username=data.get('Username')).first()
            print(user)
       
            if user and User.check_password(data.get('Password')):
                jwt_token = JWT_service.encode_JWT_token(user.id)
                if jwt_token:
                    response_json = json.dumps(JWTtokenResponse("success","Successfully logged in",jwt_token.decode()), 200, cls=JWTtokenResponseEncoder)
                    return response_json
            else:
                response_json = json.dumps(JWTtokenResponse("fail","invalid credentials",401), cls=JWTtokenResponseEncoder)
                return user
        except Exception:
             response_json = json.dumps(JWTtokenResponse("fail","try again",500), cls=JWTtokenResponseEncoder)
             return response_json
        
    @staticmethod
    def logout(data: str) -> Tuple[Dict[str, str], int]:
        if data:
            auth_token = data.split(" ")[1]
        else:
            auth_token = ''
        if auth_token:
            resp = User.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                # mark the token as blacklisted
                # return save_token(token=auth_token)
                return ""
            else:
                response_object = {
                    'status': 'fail',
                    'message': resp
                }
                return response_object, 401
        else:
            response_object = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return response_object, 403


    
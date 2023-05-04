from ..model.JWT import db
from typing import Dict, Tuple
from ..model.User import User
from ..service.User_service import User_service
from ..service.JWT_service import JWT_service
from ..responses.auth.JWTtokenResponse import JWTtokenResponse
from ..responses.user.User_Reponse import User_Response

class Auth_service():

    def login(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
        try:
            user = User.query.filter_by(Username=data.get('Username')).first()
            if user and user.check_password(data.get('Password')):
                jwt_token = JWT_service.encode_JWT_token(user.Id)
                if jwt_token:
                    response_json = JWTtokenResponse("Success","Successfully logged in",jwt_token.decode())
                    return response_json.auth_response(200)
            else:
                response_json = User_Response("fail","invalid credentials")
                response_json.auth_response(401) 
                return user
        except Exception:
             response_json = User_Response("fail","try again")
             return response_json.user_response(500)
        
    @staticmethod
    def logout(data: str) -> Tuple[Dict[str, str], int]:
        if data:
            auth_token = data.split(" ")[1]
        else:
            auth_token = ''
        if auth_token:
            resp = User.decode_auth_token(auth_token)
            if not isinstance(resp, str):
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


    
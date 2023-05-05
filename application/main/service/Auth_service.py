from ..model.JWT import db
from typing import Dict, Tuple
from ..model.User import User
from ..service.User_service import User_service
from ..service.JWT_service import JWT_service
from ..responses.auth.JWTtokenResponse import JWTtokenResponse
from ..responses.user.User_Reponse import User_Response

class Auth_service():

    @staticmethod
    def login(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
        try:
            user = User.query.filter_by(Username=data.get('Username')).first()
            if user and user.check_password(data.get('Password')):
                jwt_token = JWT_service.encode_JWT_token(user.Id)
                if jwt_token:
                    response_json = JWTtokenResponse("Success","Successfully logged in",jwt_token.decode())
                    return response_json.jwt_auth_response(200)
            else:
                response_json = JWTtokenResponse("fail","invalid credentials")
                response_json.auth_response(401) 
                return user
        except Exception:
             response_json = JWTtokenResponse("fail","try again")
             return response_json.auth_response(500)
        

        
    # TODO test loggin out
    @staticmethod
    def logout_user(data: str) -> Tuple[Dict[str, str], int]:
        if data:
            auth_token = data.split(" ")[1]
        else:
            auth_token = ''
        if auth_token:
            response = JWT_service.validate_JWT(auth_token)
            if not isinstance(response, str):
                return 
            else:
                response_object = JWTtokenResponse("fail",response)
                return response_object.auth_response(401)
        else:
            response_object = JWTtokenResponse("fail",'provide a valid authentication token')
            return response_object.auth_response(403)
    
    # get the logged in user
    @staticmethod
    def get_logged_in_user(new_request):
        auth_token = new_request.headers.get('Authorization') 
        if auth_token:
            response = JWT_service.validate_JWT(auth_token)
            if not isinstance(response, str):
                user = User.query.filter_by(Id=response).first()
                response_object = User_Response("sucess",'')
                return response_object.user_response_logged_in_user(user,200)
            response_object = JWTtokenResponse("fail",response)
            return response_object.auth_response(401)
        else:
            response_object = User_Response("fail",'provide a valid authentication token')
            return response_object.user_response(401)
        
    @staticmethod
    def verify_user_rights(new_request):
        auth_token = new_request.headers.get('Authorization') 
        if auth_token:
            response = JWT_service.validate_JWT(auth_token)
            user = User.query.filter_by(Id=response).first()
            return user
        
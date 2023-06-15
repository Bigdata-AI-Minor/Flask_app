from functools import wraps
from typing import Callable
from ..service.Auth_service import Auth_service
from ..model.DTO.User_DTO import User_DTO
from application.main.model.enums.User_roll import User_roll
from flask import request
from ..responses.user.User_Reponse import User_Response
from ..model.User import User
class Auth_Helper():
    
    # check if the user has a valid jwt_token : endpoints can only be used then
    def jwt_token_required(f) -> Callable:
        @wraps(f)
        def decorated(*args, **kwargs):
            data, status = Auth_service.get_logged_in_user(request) 
            jwt_token = data.get('data')
            if not jwt_token:
                return data, status
            return f(*args, **kwargs)
        return decorated
    
    # check if the user has sufficient rights // checken of the user niet null is ipv status 200
    def authorize(required_role: int) -> Callable:
        def decorator(f: Callable) -> Callable:
            @wraps(f)
            def decorated(*args, **kwargs):
                current_user = User.get_current_user()
                if current_user is None:
                    return  current_user, 403
                if current_user.Role != User_roll.ADMIN.value:
                    response_json = User_Response("fail","Insufficient privilege")
                    return response_json.user_response(403) 
                return f(*args, **kwargs)
            return decorated
        return decorator
    
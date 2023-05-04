from application.main import db
from functools import wraps
from typing import Callable
from ..service.Auth_service import Auth_service
from flask import request
from ..responses.auth.JWTtokenResponse import JWTtokenResponse
class Auth_Helper():

    def jwt_token_required(f) -> Callable:
        @wraps(f)
        def decorated(*args, **kwargs):

            data, status = Auth_service.get_logged_in_user(request) 
            jwt_token = data.get('data')
            if not jwt_token:
                return data, status
            return f(*args, **kwargs)
        return decorated
    
    def admin_token_required(f: Callable) -> Callable:
        @wraps(f)
        def decorated(*args, **kwargs):
            data, status = Auth_service.get_logged_in_user(request)
            token = data.get('data')
            if not token:
                return data, status
            admin = token.get('admin')
            if not admin:
                response_object = JWTtokenResponse('fail','admin token required')
                return response_object.auth_response(401)
            return f(*args, **kwargs)
        return decorated
        
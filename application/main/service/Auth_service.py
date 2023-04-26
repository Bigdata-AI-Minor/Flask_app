from ..model.JWT import db
from typing import Dict, Tuple
from ..model.User import User
from ..service.User_service import User_service
from ..service.JWT_service import JWT_service
from ..responses.auth.JWTtokenResponse import JWTtokenResponse

class Auth_service():

    def __init__(self) -> None:
        pass

    jwt_token_response = JWTtokenResponse
    # todo create a login
    def login(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
        try:
            # fetch the user data
            user = User.query.filter_by(name=data.get('name')).first()
            if user and user.check_password(data.get('password')):
                JWT_service.create_JWT()
                auth_token = User.encode_auth_token(user.id)
                if auth_token:
                    return JWTtokenResponse("success","Successfully logged in",auth_token.decode()), 200
            else:
                return JWTtokenResponse("fail","invalid credentials",401)
        except Exception:
            return JWTtokenResponse("fail","try again",500)

    
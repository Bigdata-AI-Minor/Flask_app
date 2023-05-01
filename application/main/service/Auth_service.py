from ..model.JWT import db
import flask_bcrypt
from typing import Dict, Tuple
from ..model.User import User
from ..service.User_service import User_service
from ..service.JWT_service import JWT_service
from ..responses.auth.JWTtokenResponse import JWTtokenResponse, JWTtokenResponseEncoder
import json

class Auth_service():

    def login(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
        try:
            user = User.query.filter_by(data.get('username')).first()
            if user and user.check_password(data.get('password')):
                jwt_token = JWT_service.generate_JWT(user.id)
                if jwt_token:
                    response_json = json.dumps(JWTtokenResponse("success","Successfully logged in",jwt_token.decode()), 200, cls=JWTtokenResponseEncoder)
                    return response_json
            else:
                response_json = json.dumps(JWTtokenResponse("fail","invalid credentials",401), cls=JWTtokenResponseEncoder)
                return response_json
        except Exception:
             response_json = json.dumps(JWTtokenResponse("fail","try again",500), cls=JWTtokenResponseEncoder)
             return response_json

    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        self.password_hash = flask_bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password: str) -> bool:
        return flask_bcrypt.check_password_hash(self.password_hash, password)

    
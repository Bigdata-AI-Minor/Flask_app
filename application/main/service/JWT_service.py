from ..model.JWT import JWT_token
from ..model.JWT import db
from ..config import key
import datetime

class JWT_service():

    def __init__(self) -> None:
        pass
    
    # create a JWT token
    @staticmethod
    def create_JWT(user_id: int)-> bytes:
        try:
            payload = {'expire': datetime.datetime.utcnow() + datetime.timedelta(days=30),
                       'issued': datetime.datetime.utcnow(),
                       'subject': user_id}
        except Exception as exception:
            return exception
        return JWT_token.encode(payload, key,algorithm='HS256')

    # validate the JWT token
    @staticmethod
    def validate_JWT(token: JWT_token,secret):
        try:
            payload = JWT_token.decode(token, secret, algorithms=["HS256"])
        except Exception:
            return "invalid token"
        return payload

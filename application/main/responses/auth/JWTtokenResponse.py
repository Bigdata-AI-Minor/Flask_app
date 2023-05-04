import json

class JWTtokenResponse:
    def __init__(self, status, message,Authorization):
        self.status = status
        self.message = message
        self.Authorization = Authorization

    def auth_response(self,httpstatuscode: int) -> dict:
        response_object = {
            'status': self.status,
            'message': self.message,
        }
        return response_object, httpstatuscode
      
    def jwt_auth_response(self,httpstatuscode: int) -> dict:
        response_object = {
            'status': self.status,
            'message': self.message,
            'Authorization': self.Authorization,
        }
        return response_object, httpstatuscode  


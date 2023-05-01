import json

class JWTtokenResponse:
    def __init__(self, status, message,httpstatuscode):
        self.status = status
        self.message = message
        self.httpstatuscode = httpstatuscode

class JWTtokenResponseEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, JWTtokenResponse):
            return {'status':obj.status,'message':obj.message,'httpstatuscode':obj.httpstatuscode}
        return super().default(obj)
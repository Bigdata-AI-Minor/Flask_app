class JWTtokenResponse:
    def __init__(self, status, message,httpstatuscode):
        self.status = status
        self.message = message
        self.httpstatuscode = httpstatuscode
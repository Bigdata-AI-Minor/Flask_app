class User_Response:

    def __init__(self, status: str, message: str):
        self.status = status
        self.message = message

    def user_response(self,httpstatuscode: int) -> dict:
        response_object = {
            'status': self.status,
            'message': self.message
        }
        return response_object, httpstatuscode  

    

    

    


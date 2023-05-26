class Image_Response:

    def __init__(self, status:str , message:str) -> None:
        self.status = status
        self.message = message

    def image_response(self,httpstatuscode: int) -> dict:
        response_object = {
            'status': self.status,
            'message': self.message
        }
        return response_object, httpstatuscode 
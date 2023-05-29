class Prediction_Response:

    def __init__(self, status:str, message:str) -> None:
        self.status = status
        self.message = message

    def prediction_message_response(self, httpstatuscode: int) -> dict:
        response_object = {
            'status': self.status,
            'message': self.message
        }
        return response_object, httpstatuscode 
    def prediction_response(self, prediction, httpstatuscode: int) -> dict:
        response_object = {
            'status': self.status,
            'data': {'prediction': prediction}
        }
        return response_object, httpstatuscode
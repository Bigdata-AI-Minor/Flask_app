import torch
from application.main.responses.prediction.prediction_response import Prediction_Response
from application.main.service.Classification_service import Classification_service
from typing import Dict, Tuple

model = []

class Prediction_Service():
    def __init__(self) -> None:
        model = torch.hub.load('/torch_model/model.pt', 'yolov5m', pretrained=True)
        model.eval()
        return model

    def Predict_image(data: Dict[str, str]):
        try:
            image_file = request.files['image_file']
            if not allowed_file(image_file.filename):
                return {'message': 'Only JPEG, JPG or PNG files are allowed.'}, 400
        

            results = model(data)

            results.render()  # updates results.imgs with boxes and labels
            
            return results
        except:
            response = Prediction_Response('Failed', 'Could not make a prediction, try again.')
            return Prediction_Response.prediction_message_response(500)
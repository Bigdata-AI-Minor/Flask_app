import torch
from application.main.responses.prediction.prediction_response import Prediction_Response
from application.main.service.Classification_service import Classification_service
from typing import Dict, Tuple

model = []

class Image_prediction():
    def __init__(self) -> None:
        model = torch.hub.load('/torch_model/model.pt', 'yolov5m', pretrained=True)
        model.eval()
        return model

    def Predict_image(data: Dict[str, str]):
        try:
            results = model(data)

            results.render()  # updates results.imgs with boxes and labels
            
            return results
        except:
            response = Prediction_Response('Failed', 'Could not make a prediction, try again.')
            return Prediction_Response.prediction_message_response(500)
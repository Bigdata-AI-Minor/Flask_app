import torch
import os
from application.main.responses.prediction.prediction_response import Prediction_Response
from typing import Dict
import json

class Prediction_Service():

    def Predict_image(img: Dict[str, str]):
        try:
            # use this path in native linux environment 
            # path = f'{os.path.dirname(__file__)}/../torch_model/model.pt'
            
            # use this path in docker environment 
            path = f'{os.path.dirname(__file__)}/../../../torch_model/model.pt'
            
            model = torch.hub.load(
                'ultralytics/yolov5', 
                'custom', 
                source='local', 
                path=path, 
                force_reload=True
                ) 
            results = model(img, size=640)
            
            prediction = json.loads(results.pandas().xyxy[0].to_json(orient="records"))[0]['name']
            return {'prediction': prediction }
        except:
            # response = Prediction_Response('Failed', 'Could not make a prediction, try again.')
            response = Prediction_Response('Failed', path)
            return response.prediction_message_response(500)
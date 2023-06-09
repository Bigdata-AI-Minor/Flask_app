from flask import request
from flask_restx import Resource
from ..service.Prediction_service import Prediction_Service
from ..model.DTO.Prediction_DTO import Prediction_DTO
from ..controller.Upload_controller import allowed_file
from PIL import Image
import io

dto = Prediction_DTO()

api = dto.api
upload_parser = api.parser()
upload_parser.add_argument('image_file', location='files', type='file', required=True)

@api.route('/', methods=["POST"])
class Prediction_controller(Resource):
    
    @api.expect(upload_parser, validate=True)
    @api.doc('Predict image class with image.')
    def post(self):
        image_file = request.files['image_file']
        if not allowed_file(image_file.filename):
            return {'message': 'Only JPEG, JPG or PNG files are allowed.'}, 400
        
        image_bytes = image_file.read()
        img = Image.open(io.BytesIO(image_bytes))
        
        return Prediction_Service.Predict_image(img)
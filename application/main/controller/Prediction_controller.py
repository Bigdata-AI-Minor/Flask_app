from flask import request
from flask_restx import Resource
from ..service.Prediction_service import Prediction_Service
from ..model.DTO.Classification_DTO import Classification_DTO
from ..controller.Upload_controller import allowed_file

dto = Classification_DTO()

api = dto.api
classification_dto = dto.classification_dto
upload_parser = api.parser()
upload_parser.add_argument('image_file', location='files', type='file', required=True)

@api.route('/', methods=["POST", "GET"])
class Prediction_controller(Resource):
    @api.expect(classification_dto)
    @api.doc('Create classification entity.')
    def post(self):
        
        return Prediction_Service.Predict_image(image_file.filename)
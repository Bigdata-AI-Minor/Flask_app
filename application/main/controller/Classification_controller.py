from flask import request
from flask_restx import Resource
from ..service.Classification_service import Classification_service
from ..model.DTO.Classification_DTO import Classification_DTO

dto = Classification_DTO()

api = dto.api
classification_dto = dto.classification_dto

@api.route('/', methods=["POST", "GET"])
class Classification_controller(Resource):
    @api.expect(classification_dto)
    @api.doc('Create classifcation entity.')
    def post(self):
        if request.method == "POST":
            data=request.json

            return Classification_service.create_classification(data)
    
    @api.doc('Get image entities.')
    @api.marshal_list_with(classification_dto, envelope='data')
    def get(self):
        if request.method == "GET":
            return Classification_service.get_classifications()

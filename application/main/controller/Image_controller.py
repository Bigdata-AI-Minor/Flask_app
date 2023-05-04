from flask import request
from flask_restx import Resource
from ..service.Image_service import Image_service
from ..model.DTO.Image_DTO import Image_DTO

dto = Image_DTO()

api = dto.api
image_dto = dto.image_dto
image_id_dto = dto.image_id_dto

@api.route('/', methods=["POST", "GET"])
class Image_controller(Resource):

    @api.expect(image_dto)
    @api.doc('Create image entity.')
    def post(self):
        data=request.json
        return Image_service.Create_image(data)
    
    @api.doc('Get image entities.')
    @api.marshal_list_with(image_id_dto, envelope='data')
    def get(self):
        return Image_service.get_image(None)
        
@api.route('/<int:id>', methods=["PUT", "GET", "DELETE"])
class Image_id_controller(Resource):

    @api.doc('Update image entity.')
    def put(id: int):
        data=request.json

    @api.doc('Create image entity.')
    def delete(id: int):
        data=request.json

    @api.doc('Get image entity by id.')
    def get(id: int):
        return Image_service.get_image(id)
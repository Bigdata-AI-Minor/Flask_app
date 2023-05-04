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
        
@api.route('/<int:id>/<int:classification>', methods=["PUT"])
class Image_id_update_controller(Resource):

    @api.doc('Update image entity.')
    def put(self, id: int, classification: int):
        if request.method == 'PUT':
            return Image_service.Edit_image(id, classification)
        
@api.route('/<int:id>', methods=["GET", "DELETE"])  
class Image_id_controller(Resource):

    @api.doc('Delete image entity.')
    def delete(self, id: int):
        if request.method == 'DELETE':
            return Image_service.Delete_image(id)

    @api.doc('Get image entity by id.')
    def get(id: int):
        return Image_service.get_image(id)
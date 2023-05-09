from flask import request
from flask_restx import Resource
from ..service.Image_service import Image_service
from ..model.DTO.Image_DTO import Image_DTO

dto = Image_DTO()

api = dto.api
image_dto = dto.image_dto
image_id_dto = dto.image_id_dto
image_update_dto = dto.image_put_dto

@api.route('/', methods=["POST", "GET"])
class Image_controller(Resource):

    @api.expect(image_dto)
    @api.doc('Create image entity.')
    def post(self):
        data=request.json
        return Image_service.Create_image(data)
        # convert bitstring in backend (link)
    
    @api.doc('Get image entities.')
    @api.marshal_list_with(image_id_dto, envelope='data')
    def get(self):
        return Image_service.get_images()
    
        
@api.route('/<int:id>', methods=["GET", "DELETE", "PUT"])  
class Image_id_controller(Resource):

    @api.doc('Delete image entity.')
    def delete(self, id: int):
        return Image_service.Delete_image(id)

    @api.doc('Get image entity by id.')
    @api.marshal_list_with(image_id_dto, envelope='data')
    def get(self, id: int):
        return Image_service.get_image(id)
    
    @api.expect(image_update_dto)
    @api.doc('Update image entity.')
    def put(self, id: int):
        classification = request.json['classification']
        return Image_service.Edit_image(id, classification)
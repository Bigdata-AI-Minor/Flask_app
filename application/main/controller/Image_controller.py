from flask import request
from flask_restx import Resource
from ..service.Image_service import Image_service
from ..model.DTO.Image_DTO import Image_DTO

dto = Image_DTO()

api = dto.api
image_dto = dto.image_dto

@api.route('/', methods=["POST", "GET"])
class Image_controller(Resource):

    @api.expect(image_dto)
    @api.doc('Create image entity.')
    def post(self):
        if request.method == "POST":
            data=request.json
            
            return Image_service.Create_image(data)
    
    @api.doc('Get image entities.')
    def get():
        if request.method == "GET":
            data=request.json
            return Image_service.get_images(data)
        
@api.route('/<int:id>', methods=["PUT", "GET", "DELETE"])
class Image_id_controller(Resource):

    @api.doc('Update image entity.')
    def put(id: int):
        data=request.json

    @api.doc('Create image entity.')
    def delete(id: int):
        data=request.json

    @api.doc('Get image entity by id.')
    def get(id : int):
        data=request.json
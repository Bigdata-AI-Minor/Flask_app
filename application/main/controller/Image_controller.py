from flask import request
from flask_restx import Namespace, fields, Resource
from ..service.Image_service import Image_service
# from ..model.DTO.Image_DTO import Image_DTO

api=Namespace('Images', description='Image related operations.')
image_dto = api.model('Image_DTO', {
    'classification': fields.String(attribute='classification', required=True, description='The email address'),
    'long': fields.Float(attribute='long', required=True, description='The longitude of the image taken.'),
    'lan': fields.Float(attribute='lat', required=True, description='The latitude of the image taken.'),
    'created': fields.String(attribute='created_at', required=True, description='The time created if the image taken.'),
    'bit_string': fields.String(attribute='image_bit_string', required=True, description='The the 64 bit string of the image.'),
})

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
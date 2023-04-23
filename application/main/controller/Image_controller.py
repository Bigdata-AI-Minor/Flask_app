from flask import request
from flask_restx import Namespace, fields, Resource
from ..service.Image_service import Image_service
from ..model.DTO.Image_DTO import Image_DTO

api=Namespace('Images', description='Image related operations.')
image_dto=api.model(Image_DTO, {
    'Classification': fields.String(required=True, description='The email address'),
    'Long': fields.Float(required=True, description='The longitude of the image taken.'),
    'lan': fields.Float(required=True, description='The latitude of the image taken.'),
    'created': fields.String(required=True, description='The time created if the image taken.'),
})


@api.route('/', methods=["POST", "GET"])
class Image_controller(Resource):

    @api.doc('Create image entity.')
    def post():
        data=request.json
    
    @api.doc('Get image entities.')
    def get():
        data=request.json
        
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
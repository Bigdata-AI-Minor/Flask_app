from flask import Flask, request
from flask_restx import Namespace, fields, Resource
from ..service.Image_service import Image_service
from ..model.DTO.Image_DTO import Image_DTO

api = Namespace('images', description='Image related operations.')
user_auth = api.model('auth_details', {
    'Classification': fields.String(required = True, description = 'The email address'),
    'Long': fields.Float(required = True, description = 'The longitude of the image taken.'),
    'lan': fields.Float(required = True, description = 'The latitude of the image taken.'),
    'created': fields.String(required = True, description = 'The time created if the image taken.'),
})


class Auth_controller:

    @api.route('/', method = ["POST"])
    @api.doc('Create image entity.')
    def create_image():
        data = request.json


    @api.route('/<int:id>', method = ["PUT"])
    @api.doc('Update image entity.')
    def update_image(string : id):
        data = request.json


    @api.route('/<int:id>', method = ["DELETE"])
    @api.doc('Create image entity.')
    def delete_image(string : id):
        data = request.json


    @api.route('/images', method = ["GET"])
    @api.doc('Get image entities.')
    def get_images():
        data = request.json
        

    @api.route('/<int:id>', method = ["GET"])
    @api.doc('Get image entity.')
    def get_image(string : id):
        data = request.json
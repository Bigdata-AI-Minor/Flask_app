from flask import Flask, request
from flask_restx import Resource
from ..service.Image_service import Image_service
from ..model.DTO.Image_DTO import Image_DTO

api = Flask(__name__)

class Auth_controller:

    @api.route('/images', method = ["POST"])
    @api.doc('Create image entity.')
    def create_image():
        data = request.json


    @api.route('/images/<int:id>', method = ["PUT"])
    @api.doc('Update image entity.')
    def update_image(string : id):
        data = request.json


    @api.route('/images/<int:id>', method = ["DELETE"])
    @api.doc('Create image entity.')
    def delete_image(string : id):
        data = request.json


    @api.route('/images', method = ["GET"])
    @api.doc('Get image entities.')
    def get_images():
        data = request.json
        

    @api.route('/images/<int:id>', method = ["GET"])
    @api.doc('Get image entity.')
    def get_image(string : id):
        data = request.json
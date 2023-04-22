from flask import Flask, request
from flask_restx import Namespace, fields, Resource
from ..service.User_service import User_service
from ..model.DTO.User_DTO import User_DTO

api = Namespace('users', description = 'User related operations')
user = api.model(User_DTO, {
    'name': fields.String(required = True, description = 'The name of the user.'),
    'userRoll': fields.String(required = True, description = 'The user password.'),
})

class Auth_controller:

    @api.route('/', method = ["POST"])
    def create_user():
        data = request.json


    @api.route('/<int:id>', method = ["PUT"])
    def update_user(string : id):
        data = request.json


    @api.route('/<int:id>', method = ["DELETE"])
    def delete_user(string : id):
        data = request.json


    @api.route('/', method = ["GET"])
    def get_users():
        data = request.json
        

    @api.route('/<int:id>', method = ["GET"])
    def get_user(string : id):
        data = request.json
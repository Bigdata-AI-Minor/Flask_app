from flask import request
from flask_restx import Namespace, fields, Resource
from ..service.User_service import User_service
from ..model.DTO.User_DTO import User_DTO

api=Namespace('Users', description='User related operations')
user_dto=api.model(User_DTO, {
    'name': fields.String(required=True, description='The name of the user.'),
    'userRoll': fields.String(required=True, description='The user password.'),
})

@api.route('/', methods=["POST", "GET"])
class User_controller(Resource):

    @api.doc('Create user')
    def post():
        data=request.json

    @api.doc('Get users.')
    def get():
        data=request.json

@api.route('/<int:id>', methods=["DELETE", "PUT", "GET"])
class User_id_controller(Resource):

    @api.doc('Update user entity by id.')
    def put(id: int):
        data=request.json

    @api.doc('Delete user entity by id.')
    def delete(id: int):
        data=request.json

    @api.doc('Get user entity by id.')
    def get(id: int):
        data=request.json
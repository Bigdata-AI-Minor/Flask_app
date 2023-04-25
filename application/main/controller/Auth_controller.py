from flask import request
from flask_restx import Namespace, fields, Resource
from ..service.Auth_service import Auth_service
from ..model.DTO.Auth_DTO import Auth_DTO

api=Namespace('Auth', description='Authentication related operations')
auth_dto=api.model(Auth_DTO, {
    'name': fields.String(required=True, description='The name of the user'),
    'password': fields.String(required=True, description='The user password '),
})

@api.route('/login', methods=["POST"])
class Login_controller(Resource):

    @api.doc('Login user.')
    def post():
        data=request.json

@api.route('/logout', methods=["POST"])
class Logout_controller(Resource):

    @api.doc('Logout user.')
    def post():
        data=request.json
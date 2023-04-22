from flask import Flask, request
from flask_restx import Namespace, fields, Resource
from ..service.Auth_service import Auth_service
from ..model.DTO.Auth_DTO import Auth_DTO

api = Namespace('auth', description='authentication related operations')
user_auth = api.model(Auth_DTO, {
    'name': fields.String(required = True, description = 'The name of the user'),
    'password': fields.String(required = True, description = 'The user password '),
})


class Auth_controller:

    @api.route('/login', method = ["POST"])
    @api.doc('Login user')
    def Login():
        data = request.json

    @api.route('/logout', method = ["PUT"])
    @api.doc('Logout user.')
    def Logout():
        data = request.json
        

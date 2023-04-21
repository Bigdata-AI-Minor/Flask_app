from flask import Flask, request
from flask_restx import Resource
from ..service.Auth_service import Auth_service
from ..model.DTO.Auth_DTO import Auth_DTO

api = Flask(__name__)

class Auth_controller:

    @api.route('/login', method = ["POST"])
    @api.doc('Login user')
    def Login():
        data = request.json

    @api.route('/logout', method = ["POST"])
    @api.doc('Log out user.')
    def Logout():
        data = request.json
        

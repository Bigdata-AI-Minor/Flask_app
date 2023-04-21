from flask import Flask, request
from flask_restx import Resource
from ..service.User_service import User_service
from ..model.DTO.User_DTO import User_DTO

api = Flask(__name__)

class Auth_controller:

    @api.route('/users', method = ["POST"])
    def create_user():
        data = request.json


    @api.route('/user/<int:id>', method = ["PUT"])
    def update_user(string : id):
        data = request.json


    @api.route('/users/<int:id>', method = ["DELETE"])
    def delete_user(string : id):
        data = request.json


    @api.route('/users', method = ["GET"])
    def get_users():
        data = request.json
        

    @api.route('/users/<int:id>', method = ["GET"])
    def get_user(string : id):
        data = request.json
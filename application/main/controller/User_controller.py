from flask import request
from flask_restx import Namespace, fields, Resource
from ..service.User_service import User_service
from ..model.DTO.User_DTO import User_DTO
from typing import Dict, Tuple


dto = User_DTO()
api = dto.api
user_dto = dto.user_dto

@api.route('/', methods=["POST", "GET"])
class User_controller(Resource):

    @api.doc('Create user')
    @api.expect(user_dto,validate=True)
    def post(self) -> Tuple[Dict[str, str], int]:
        data=request.json
        return User_service.create_user(data)

    @api.doc('Get users.')
    @api.marshal_list_with(user_dto, envelope='data')
    def get(self):
        return User_service.get_users()

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
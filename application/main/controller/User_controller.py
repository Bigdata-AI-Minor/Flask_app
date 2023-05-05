from flask import request
from flask_restx import Resource
from ..service.User_service import User_service
from ..model.DTO.User_DTO import User_DTO
from typing import Dict, Tuple
from ..helper.auth_helper import Auth_Helper 
from application.main.model.enums.User_roll import User_roll


dto = User_DTO()
api = dto.api

@api.route('/', methods=["POST", "GET"])
class User_controller(Resource):
    
    @api.doc('Create user')
    @Auth_Helper.jwt_token_required
    @api.expect(dto.user_create_dto,validate=True)
    def post(self) -> Tuple[Dict[str, str], int]:
        return User_service.create_user(request.json)
    
    # only admin can use this endpoint
    @api.doc('Get users.')
    @Auth_Helper.jwt_token_required
    @Auth_Helper.verify_rights(User_roll.ADMIN.value)
    @api.marshal_list_with(dto.user_dto, envelope='data')
    def get(self):
        return User_service.get_users()

@api.route('/<int:id>', methods=["DELETE", "PUT", "GET"])
class User_id_controller(Resource):

    @api.doc('Update user entity by id.')
    @Auth_Helper.jwt_token_required
    @Auth_Helper.verify_rights(User_roll.ADMIN.value)
    @api.expect(dto.user_create_dto,validate=True)
    def put(self, id: int) -> Tuple[Dict[str, str], int]:
        return User_service.edit_user_by_Id(id,request.json)

    @api.doc('Delete user entity by id.')
    @Auth_Helper.jwt_token_required
    @Auth_Helper.verify_rights(User_roll.ADMIN.value)
    def delete(self,id: int):
        return User_service.delete_user_by_id(id)

    @api.doc('Get user entity by id.')
    @Auth_Helper.jwt_token_required
    @Auth_Helper.verify_rights(User_roll.ADMIN.value)
    @api.marshal_list_with(dto.user_dto, envelope='data')
    def get(self, id: int):
        return User_service.get_user_by_id(id)
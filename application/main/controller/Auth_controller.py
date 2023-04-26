from flask import request
from flask_restx import Resource
from ..service.Auth_service import Auth_service
from ..model.DTO.Auth_DTO import Auth_DTO
from typing import Dict, Tuple
    
dto = Auth_DTO()

api = dto.api
auth_dto = dto.auth_dto


@api.route('/login', methods=["POST"])
class Login_controller(Resource):
    @api.doc('Login user.')
    @api.expect(auth_dto,validate=True)
    def post(self) -> Tuple[Dict[str, str], int]:
        return Auth_service.login(request.json)

@api.route('/logout', methods=["POST"])
class Logout_controller(Resource):

    @api.doc('Logout user.')
    def post():
        data=request.json
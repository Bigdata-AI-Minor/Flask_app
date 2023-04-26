from flask_restx import Namespace, fields

class User_DTO():
      api = Namespace('Users', description='User related information.')
      user_dto = api.model('User', {
        'id': fields.String(attribute='classification', required=True, description='The Id'),
        'username': fields.String(attribute='string', required=True, description='The username of the user.'),
        'password': fields.String(attribute='lat', required=True, description='The password of the user'),
        'role': fields.Integer(attribute='created_at', required=True, description='The role of the user'),
        'jwt_token': fields.String(attribute='bit_string', required=True, description='The jwt token of the user'),
    })
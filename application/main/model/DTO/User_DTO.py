from flask_restx import Namespace, fields

class User_DTO():
      api = Namespace('Users', description='User related information.')
      user_dto = api.model('User', {
        'Id': fields.Integer(attribute='Integer', required=True, description='The Id'),
        'Username': fields.String(attribute='string', required=True, description='The username of the user.'),
        'Password': fields.String(attribute='string', required=True, description='The password of the user'),
        'Role': fields.Integer(attribute='Integer', required=True, description='The role of the user'),
        # 'Jwt_token': fields.String(attribute='bit_string', required=True, description='The jwt token of the user'),
    })
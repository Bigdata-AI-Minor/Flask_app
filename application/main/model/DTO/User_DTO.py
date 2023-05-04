from flask_restx import Namespace, fields

class User_DTO():
      api = Namespace('Users', description='User related information.')
      user_dto = api.model('User', {
        'Id': fields.Integer(attribute='Id', required=True, description='The Id'),
        'Username': fields.String(attribute='Username', required=True, description='The username of the user.'),
        'Role': fields.Integer(attribute='Role', required=True, description='The role of the user'),
    })
      
      user_create_dto = api.model('User', {
        'Password': fields.String(attribute='Password', required=True, description='The password of the user'),
    })
      
      
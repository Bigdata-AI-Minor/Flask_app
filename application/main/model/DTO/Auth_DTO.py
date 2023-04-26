from flask_restx import Namespace, fields

class Auth_DTO():
    api = Namespace('auth', description='authentication related operations')
    auth_dto = api.model('auth_details', {
        'name': fields.String(required=True, description='The name'),
        'password': fields.String(required=True, description='The user password '),
    })
        
from flask_restx import Namespace, fields

class Auth_DTO():
    api = Namespace('auth', description='authentication related operations')
    auth_dto = api.model('auth_details', {
        'Username': fields.String(required=True, description='The username of the user'),
        'Password': fields.String(required=True, description='The password of the user '),
    })
        
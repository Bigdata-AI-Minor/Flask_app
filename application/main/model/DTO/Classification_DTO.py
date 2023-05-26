from flask_restx import Namespace, fields

class Classification_DTO():
    api = Namespace('Classifications', description='Classification related operations.')

    # classification_dto = api.model('Classification', {
    #     'id': fields.Integer(required=True, description='The classification id'),
    #     'classification': fields.String(required=True, description='The classification name'),
    # })

    classification_dto = api.model('Classification', {
        'classification': fields.String(required=True, description='The classification name'),
    })
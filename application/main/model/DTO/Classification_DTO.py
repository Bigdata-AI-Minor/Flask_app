from flask_restx import Namespace, fields

class Classification_DTO():
    api = Namespace('Classifications', description='Classification related operations.')
    classification_dto = api.model('Classification', {
        'id': fields.Integer(readOnly=True, description='The classification identifier'),
        'classification': fields.String(required=True, description='The classification name'),
    })
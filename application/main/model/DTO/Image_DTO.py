from flask_restx import Namespace, fields
# from .Classification_DTO import Classification_DTO

class Image_DTO():
    api = Namespace('Images', description='Image related operations.')
    image_dto = api.model('Image', {
        # 'classification': fields.Nested(Classification_DTO.classification_dto, required=True, description='The classification of the image.'),
        'classification': fields.Integer(attribute='classification', required=True, description='The classification of the image.'),
        'long': fields.Float(attribute='long', required=True, description='The longitude of the image taken.'),
        'lan': fields.Float(attribute='lat', required=True, description='The latitude of the image taken.'),
        'created': fields.String(attribute='created_at', required=True, description='The time created if the image taken.'),
        'bit_string': fields.String(attribute='bit_string', required=True, description='The the 64 bit string of the image.'),
    })
from flask_restx import Namespace, fields

class Upload_DTO():
    api = Namespace('Image bit strings', description='Bit string related operations.')

    upload_dto = api.model('Image_bit_string', {
        'id': fields.Integer(attribute='id', required=True, description='The id of the image bit string.'),
        'bit_string': fields.String(attribute='bit_string', required=True, description='The bit string of the image.'),
    })
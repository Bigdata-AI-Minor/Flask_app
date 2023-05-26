from flask_restx import Namespace, fields

class Image_DTO():
    api = Namespace('Images', description='Image related operations.')


    image_dto = api.model('Image', {
        'image_bit_string_id': fields.Integer(attribute='image_bit_string_id', required=True, description='The id of the bit string image.'),
        'classification': fields.Integer(attribute='classification', required=True, description='The classification(1 = plastic, 2 = cardboard, 3 = metal, 4 = other)'),
        'long': fields.Float(attribute='long', required=True, description='The longitude of the image taken.'),
        'lan': fields.Float(attribute='lan', required=True, description='The latitude of the image taken.'),
        'created': fields.String(attribute='created', required=True, description='The time created if the image taken.'),
    })

    image_id_dto = api.model('Image_id_dto', {
        'id': fields.Integer(attribute='id', required=True, description='The id of the image.'),
        'image_bit_string_id': fields.Integer(attribute='image_bit_string_id', required=True, description='The id of the bit string image.'),
        'classification': fields.Integer(attribute='classification', required=True, description='The classification(1 = plastic, 2 = cardboard, 3 = metal, 4 = other)'),
        'long': fields.Float(attribute='long', required=True, description='The longitude of the image taken.'),
        'lan': fields.Float(attribute='lan', required=True, description='The latitude of the image taken.'),
        'created': fields.String(attribute='created', required=True, description='The time created if the image taken.'),
    })

    image_put_dto = api.model('image_put_dto', {
        'classification': fields.Integer(attribute='classification', required=True, description='The classification(1 = plastic, 2 = cardboard, 3 = metal, 4 = other)'),
                })

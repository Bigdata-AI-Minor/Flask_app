from flask_restx import namespace, fields

class Prediction_DTO():
    api = namespace('Predictions', description='Classification prediction related operations')
    prediction_dto = api.model('prediction', {
        'prediction': fields.String(attribute='created', required=True, description='The time created if the image taken.')
    })
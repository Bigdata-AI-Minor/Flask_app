from flask_restx import Namespace, fields

class Prediction_DTO():
    api = Namespace('Predictions', description='Classification prediction related operations')
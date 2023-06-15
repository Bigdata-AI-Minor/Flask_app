from flask_restx import Api
from flask import Blueprint

from .main.controller.User_controller import api as user_ns
from .main.controller.Auth_controller import api as auth_ns
from .main.controller.Image_controller import api as img_ns
from .main.controller.Upload_controller import api as upload_ns
from .main.controller.Classification_controller import api as classification_ns
from .main.controller.Prediction_controller import api as prediction_ns


blueprint=Blueprint('api', __name__)
authorizations={
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}

api=Api(
    blueprint,
    title='Flask application StadsJutters',
    version='1.0',
    description='a flask restplus (restx) web service application for the pilot project StadsJutters',
    authorizations=authorizations,
    security='apikey'
)

api.add_namespace(user_ns, path='/users')
api.add_namespace(auth_ns, path='/auth')
api.add_namespace(upload_ns, path='/bitstrings')
api.add_namespace(img_ns, path='/images')
api.add_namespace(classification_ns, path='/classification')
api.add_namespace(prediction_ns, path='/prediction')
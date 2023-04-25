import os
import unittest

from flask_migrate import Migrate

from application import blueprint
from application.main import create_app, db
from application.main.model import JWT, Image, User, User_roll, Classification

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.register_blueprint(blueprint)

app.app_context().push()

migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    return dict(
        db=db, 
        User=User, 
        Image=Image,
        Jwt=JWT,
        Class=Classification,
        User_roll=User_roll
        )

# TODO create test command for populate database
# @app.cli.command()
# def test():
#     """Runs the unit tests."""
#     tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
#     result = unittest.TextTestRunner(verbosity=2).run(tests)
#     if result.wasSuccessful():
#         return 0
#     return 1
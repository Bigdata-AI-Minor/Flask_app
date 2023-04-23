import os
import unittest

from flask_migrate import Migrate

from application import blueprint
from application.main import create_app, db
from application.main.Database import User_repo, Image_repo, JWT_repo, UserRoll_repo, Class_repo

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.register_blueprint(blueprint)

app.app_context().push()

migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    return dict(
        db=db, 
        User=User_repo, 
        Image=Image_repo,
        Jwt=JWT_repo,
        Class=Class_repo,
        User_roll=UserRoll_repo
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
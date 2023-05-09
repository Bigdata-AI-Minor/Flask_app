import os

from flask_migrate import Migrate

from application import blueprint
from application.main import create_app, db
from application.main.model import JWT, Image, User, Classification
from application.main.model.enums.User_roll import User_roll
from application.main.model.User import User

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
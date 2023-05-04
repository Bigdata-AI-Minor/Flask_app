import os

from flask_migrate import Migrate

from application import blueprint
from application.main import create_app, db
from application.main.model import JWT, Image, User, Classification
from application.main.model.enums.User_roll import User_roll
from application.main.model.User import User
from application.main.helper.Testdata import Testdata

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.register_blueprint(blueprint)

app.app_context().push()

migrate = Migrate(app, db)
# create tables in the database that do not exists uncomment '# test_service.populate_database()' to populate database with info
# migrate.db.create_all()
# populate db
# test_service = Testdata()
# test_service.populate_database()


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
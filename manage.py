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
migrate.db.create_all()

# populate db with users
def populate_database():
    admin_user = User(Name='admin2', Password='password', Role=User_roll.ADMIN.value,Jwt_token='123')
    volunteer_user = User(Name='volunteer', Password='password', Role=User_roll.VOLUNTEER.value,Jwt_token='123')
    db.session.add_all([admin_user])
    db.session.commit()
    return

# populate_database()

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
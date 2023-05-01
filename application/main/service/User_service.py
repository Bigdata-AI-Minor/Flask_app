from ..model.User import User
from ..model.User import db

class User_service():

    def __init__(self) -> None:
        pass

    def Create_user(user: User):
        return ""

    def Delete_user(id: str):
        return ""
    
    def Edit_user(id:  str, image: User):
        return ""

    def get_user_by_id(id: str):
        try:
            return User.query.filter_by(name=db.get('Id')).first()
        except Exception as e:
             return e
    
    def get_user_by_name(id: str):
        try:
            return User.query.filter_by(name=db.get('username')).first()
        except Exception as e:
             return e
    
    def get_users():
        return ""
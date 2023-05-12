from .. import db
import datetime
import jwt


class BlacklistJwtToken(db.Model):
    __tablename__ = 'blacklistjwt_tokens'

    Id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    token = db.Column(db.String(100), unique=True, nullable=False)
    blacklisted_on = db.Column(db.DateTime, nullable=False)

    def __init__(self, token):
        self.token = token
        self.blacklisted_on = datetime.datetime.now()

    # check if the jwt token has been blacklisted
    @staticmethod
    def check_blacklist(auth_token: jwt) -> bool:
        return bool(BlacklistJwtToken.query.filter_by(token=str(auth_token)).first())

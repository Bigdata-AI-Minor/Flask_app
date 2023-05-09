from ..model.User import db
from ..model.BlacklistJwt import BlacklistJwtToken
from typing import Dict, Tuple
import jwt
from ..responses.auth.JWTtokenResponse import JWTtokenResponse

class BlacklistJwt_Service():
    # saven jwt_token in the database
    def save_jwt_token(token: jwt) -> Tuple[Dict[str, str], int]:
        blacklist_token = BlacklistJwtToken(token)
        try:
            db.session.add(blacklist_token)
            db.session.commit()
            print('hierboven is het opgeslagen in de database en hieronder is de response')
            response_json = JWTtokenResponse("Success","logged out")
            return response_json.jwt_auth_response(200)
        except Exception as exception:
            response_json = JWTtokenResponse('fail', f'Internal server error: {exception}')
            return response_json.jwt_auth_response(500)
    

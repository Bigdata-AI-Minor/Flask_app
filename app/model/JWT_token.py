from Entity import Entity

class JWT_token(Entity):
    def __init__(self):
        Entity.__init__(self, "jwt")
        
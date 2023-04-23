from .Entity import Entity

class JWT_token(Entity):
    def __init__(self, id, userRoll, name):
        Entity.__init__(self, "jwt")
        self.Id=id
        self.UserRoll=userRoll
        self.Name=name
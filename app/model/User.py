from Entity import Entity

class User(Entity):
    def __init__(self, id, name, password, role, jwt_token):
        Entity.__init__(self, "user")
        self.id = id
        self.name = name
        self.password = password
        self.role = role
        self.jwt = jwt_token
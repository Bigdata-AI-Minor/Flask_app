from Entity_DTO import Entity_DTO

class User_DTO(Entity_DTO):
    def __init__(self, name, role, jwt_token):
        Entity_DTO.__init__(self, "user")
        self.name = name
        self.role = role
        self.jwt = jwt_token
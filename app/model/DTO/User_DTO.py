from Entity_DTO import Entity_DTO

class User_DTO(Entity_DTO):
    def __init__(self, name, role):
        Entity_DTO.__init__(self, "user")
        self.Name = name
        self.Role = role
from .Entity import Entity

class User(Entity):
    def __init__(self, id, name, password, role):
        Entity.__init__(self, "User")
        self.Id=id
        self.Name=name
        self.Password=password
        self.Role=role
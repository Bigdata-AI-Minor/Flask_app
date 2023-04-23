from .Entity_DTO import Entity_DTO

class Auth_DTO(Entity_DTO):
    def __init__(self, classification, long, lan, dateTime):
        Entity_DTO.__init__(self, "Auth")
        self.Classification=classification
        self.Long=long
        self.Lan=lan
        self.DateTime=dateTime
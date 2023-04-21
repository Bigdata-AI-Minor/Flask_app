from Entity_DTO import Entity_DTO
from datetime import datetime

class Image_DTO(Entity_DTO):
    def __init__(self, classification, long, lan, dateTime):
        Entity_DTO.__init__(self, "image")
        self.classification = classification
        self.long = long
        self.lan = lan
        self.created = dateTime
from .Entity_DTO import Entity_DTO
from datetime import datetime

class Image_DTO(Entity_DTO):
    def __init__(self, classification, long, lan, dateTime, bitString):
        Entity_DTO.__init__(self, "image")
        self.Classification=classification
        self.Long=long
        self.Lan=lan
        self.Created=dateTime
        self.BitString=bitString
from .Entity import Entity
from datetime import datetime

class Image(Entity):
    def __init__(self, id, classification, long, lan, created, bit_string):
        Entity.__init__(self, "image")
        self.Id=id
        self.Classification=classification
        self.Long=long
        self.Lan=lan
        self.Created=created
        self.BitString=bit_string

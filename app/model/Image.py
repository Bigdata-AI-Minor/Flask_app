from Entity import Entity
from datetime import datetime

class Image(Entity):
    def __init__(self, id, classification, long, lan, dateTime):
        Entity.__init__(self, "image")
        self.id = id
        self.classification = classification
        self.long = long
        self.lan = lan
        self.created = dateTime
# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item
# example n_to = the room object
class Room():
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = []
    
    def addItem(self, item):
           self.items.append(item)

    def removeItem(self, item, player):
        if item in self.items:
            self.items.remove(item)
            player.addItem(item)


    def __str__(self):
        return f"{self.name}"

    
    
        

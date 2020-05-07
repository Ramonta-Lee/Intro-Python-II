# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room
class Player():

    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []

    def PrintInventory(self):
        if len(self.items) == 0:
            print("No items 🤷‍♀️")
        
        for item in self.items:
            print(item.name)

    def __str__(self):
        return f"{self.name} is at the {self. current_room.name}"

    def addItem(self, item):
        self.items.append(item)

    def removeItem(self, item):
        self.current_room.addItem(item)
        self.items.remove(item)

          
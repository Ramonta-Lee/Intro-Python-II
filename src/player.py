# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room
from print_wrapper import PrintWrapper
class Player():

    def __init__(self, name, current_room):
        self.player_name = name
        self.current_room = current_room
        self.items = []

    def PrintInventory(self):
        if len(self.items) == 0:
            PrintWrapper("No items")
        
        for item in self.items:
            print(item.name)

    def __str__(self):
        return f"{self.player_name} is in the {self. current_room.name}"

    def addItem(self, item):
        self.items.append(item)

    def removeItem(self, item):
        if item in self.items:
            self.current_room.addItem(item)
            self.items.remove(item)

          
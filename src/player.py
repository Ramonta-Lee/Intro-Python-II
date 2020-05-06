# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room
class Player():
     def __init__(self, name, current_room, items=[]):
         # super().__init__(self, room_name, room_description)
         self.player_name = name
         self.current_room = current_room
         self.items = items

     def __str__(self):
          return f"{self.player_name} is in the {self.current_room.name}"

          
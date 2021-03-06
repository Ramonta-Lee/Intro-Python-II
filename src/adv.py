import textwrap
from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
   'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

'''
My player object: 
object (class) = player
attributes = name, 
methods = move()

'''
my_player = Player("John", room["outside"])
print("Game Instructions: q = quit, n = north, s = south, e = east, w = west")

while True: # LOOP
    # The while true is the REPL parser that runs the game until the loop is broken.
    user_input = input(f"{my_player}, enter a movement command...") # READ
    
    if user_input == "n":
        # Example: if the current room has an n_to then the player's current room is set to where n_to points
        # player.current_room stores the location of the player
        if my_player.current_room.n_to: # EVAL
            my_player.current_room = my_player.current_room.n_to
            print(my_player.current_room.description) # PRINT
    
        else:
            print("There is no path in that direction")

    if user_input == "s":
        if my_player.current_room.s_to:
            my_player.current_room = my_player.current_room.s_to
            print(my_player.current_room.description)
    
        else:
            print("There is no path in that direction")

    if user_input == "e":
        if my_player.current_room.e_to:
            my_player.current_room = my_player.current_room.e_to
            print(my_player.current_room.description)
    
        else:
            print("There is no path in that direction")

    if user_input == "w":
        if my_player.current_room.w_to:
            my_player.current_room = my_player.current_room.w_to
            print(my_player.current_room.description)
    
        else:
            print("There is no path in that direction")

    if user_input == "q":
        exit(0)


        # if "n" in room[my_player.current_room].Door():
        #     pass
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

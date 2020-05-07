import textwrap
from room import Room
from player import Player
from item import Item
from print_wrapper import PrintWrapper
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

# Declare all items

item = {
    'Sword': Item("Wooden Sword", "This is but a child's sword. You will need more than this to best the cave"),

    'Shovel': Item("Shovel", "Best for digging for gold or your grave"),

    'Gold': Item("Gold", "Shiny objects can get you what you need"),

    'Axe': Item("Golden Axe", "A mighty fine weapon")
}


# room items

room['outside'].addItem(item['Sword'])
room['foyer'].addItem(item["Shovel"])
room['foyer'].addItem(item["Gold"])
room['overlook'].addItem(item["Axe"])



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
PrintWrapper("Game Instructions: q = quit, n = north, s = south, e = east, w = west")

while True: # LOOP
    # The while true is the REPL parser that runs the game until the loop is broken.
    # my player prints the player object
    user_input = input(f"{my_player}, enter a movement command...") # READ
    
    if user_input == "n":
        # Example: if the current room has an n_to then the player's current room is set to where n_to points
        # player.current_room stores the location of the player
        if my_player.current_room.n_to: # EVAL
            my_player.current_room = my_player.current_room.n_to
            PrintWrapper(my_player.current_room.description) # PRINT
    
        else:
            PrintWrapper("There is no path in that direction")

    if user_input == "s":
        if my_player.current_room.s_to:
            my_player.current_room = my_player.current_room.s_to
            PrintWrapper(my_player.current_room.description)
    
        else:
            PrintWrapper("There is no path in that direction")

    if user_input == "e":
        if my_player.current_room.e_to:
            my_player.current_room = my_player.current_room.e_to
            PrintWrapper(my_player.current_room.description)
    
        else:
            PrintWrapper("There is no path in that direction")

    if user_input == "w":
        if my_player.current_room.w_to:
            my_player.current_room = my_player.current_room.w_to
            PrintWrapper(my_player.current_room.description)
    
        else:
            PrintWrapper("There is no path in that direction")

    # Searching 

    # if you add an 'or' statement to option the input, it will always PrintWrapper the inventory????

    if user_input == "inv":
        my_player.PrintInventory()
    
    if user_input == "look":
        for item in my_player.current_room.items:
            PrintWrapper(f"\t Item: {item.name},\n\t {item.description}")

    if user_input == "take":
        stuff = my_player.current_room.items
        if len(stuff) > 0:
            for item in stuff:
                my_player.addItem(item)
                PrintWrapper(item.name)
               
        
        else:
            PrintWrapper(f"\t There is nothing to get.\n")
        

    if user_input == "q":
        exit(0)


       
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

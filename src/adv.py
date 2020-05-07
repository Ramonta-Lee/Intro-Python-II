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

    'graveyard': Room("Graveyard", """You've entered the graveyard, dig your grave""")
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
room['graveyard'].n_to = room['outside']
room['outside'].s_to = room['graveyard']

# Declare all items

item = {
    'Sword': Item("Sword", "This is but a child's sword. You will need more than this to best the cave"),

    'Shovel': Item("Shovel", "Best for digging for gold or your grave"),

    'Gold': Item("Gold", "Shiny objects can get you what you need"),

    'Axe': Item("Axe", "A Golden Axe! A mighty fine weapon")
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

# this print statement changes the color of the terminal
print("\033[1;36;40m \n")

PName = input("Welcome brave and adventurous challenger, please tell me your name...")

my_player = Player(PName, room["outside"])
print(f"""Welcome {my_player.name} to Cave Quest! The journey ahead is long and dreary and you'll find yourself weak, and weary but do not give up!\nFor what lies ahead is beyond your wildest dreams. Game Instructions: q = quit, n = north, s = south, e = east, w = west
    """)

done = False

while not done: # LOOP
    # The while true is the REPL parser that runs the game until the loop is broken.
    # my player prints the player object

    user_input = input(f"{my_player}, enter a movement command...").lower().split(" ") # READ


    if len(user_input) > 2 or len(user_input) < 1:
        print("I do not understand your command")
        continue

    if len(user_input) == 1:
        cmd = user_input[0]

        if cmd == "n":
            # Example: if the current room has an n_to then the player's current room is set to where n_to points
            # player.current_room stores the location of the player
            if my_player.current_room.n_to: # EVAL
                my_player.current_room = my_player.current_room.n_to
                print(my_player.current_room.description) # PRINT
        
            else:
                print("There is no path in that direction")

        if cmd == "s":
            if my_player.current_room.s_to:
                my_player.current_room = my_player.current_room.s_to
                print(my_player.current_room.description)
        
            else:
                print("There is no path in that direction")

        if cmd == "e":
            if my_player.current_room.e_to:
                my_player.current_room = my_player.current_room.e_to
                print(my_player.current_room.description)
        
            else:
                print("There is no path in that direction")

        if cmd == "w":
            if my_player.current_room.w_to:
                my_player.current_room = my_player.current_room.w_to
                print(my_player.current_room.description)
        
            else:
                print("There is no path in that direction")

        # Searching 

        # if you add an 'or' statement to option the input, it will always print the inventory????

        if cmd == "inv":
            my_player.PrintInventory()
        
        if cmd == "look":
            for item in my_player.current_room.items:
                print(f"\t Item: {item.name},\n\t {item.description}")

            stuff = my_player.current_room.items
            if len(stuff) == 0:
                print(f"\t There is nothing to get.\n")

        if cmd == "q" or cmd == "quit":
            done = True
       

    # two word commands

    if len(user_input) == 2:
        cmd = user_input[0]
        thing = user_input[1]
        stuff = my_player.current_room.items
        # if len(stuff) == 0:
        #     print(f"\t There is nothing to get")
        if cmd == "take":
            for item in stuff:
                # getattr takes in two arguments the object you're looking in and an attribute/key it has
                # hasattr takes in two arguments the object and the attribute but it only checks if the attr exists.
                if thing == getattr(item, "name").lower():
                    my_player.addItem(item)
                    my_player.current_room.removeItem(item)
                    print(f"\t you have obtained {thing}")

                elif thing != getattr(item, "name").lower():
                    print("Already gone 🤦‍♀️")
                else:
                    print(f"\t There is nothing to get.")

        if cmd == "drop":
            if len(my_player.items) > 0:
                for item in my_player.items:
                    if thing == getattr(item, "name").lower():
                        my_player.removeItem(item)
                        print(f"\t you have dropped {thing}")

            elif len(my_player.items) == 0:
                print(f"\t you do not have this {thing} ")



       
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

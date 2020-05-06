from room import Room

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
class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def __str__(self):
        return f"Player {self.name} is in ${self.location} room"

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# x If the user enters "q", quit the game.

while True:
    selection = input("Select the number of a department or type 'exit' to leave: ")
    if selection == "q":
        print("My sword I need no longer. Then evening wind will carry me home.")
        break
​
    # add error handling so that when a user inputs a department for a non-existent
    # department, we'll notify them that that department doesn't exist
    try:
        # casting might cause an error
        selection = int(selection)
        if selection >= len(store.departments):
            print("That's not a valid department")
        elif selection >= 0 and selection < len(store.departments):
            print(f"{store.departments[selection]}")
        else:
            print("Department numbers are positive")
    except ValueError:
        # the user didn't give us a value that could be cast to a number
        print("Please enter your choice as a number")
​
    # when should we break out of this loop?
    # let's let the user type "exit" into the selection to have them leave 
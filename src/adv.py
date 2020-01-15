from room import Room
from player import Player
from item import Item
from textwrap import fill

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

# Declares Items

item = {
    'coins': Item("coins", "shiny gold medalians"),
    'sword': Item("sword", "an old iron sword"),
    'mouse': Item("mouse", "small rodent"),
    'rocks': Item("rocks", "just ordinary rocks"),
    'axe': Item("axe", "sturdy wooden handled axe"),
    'empty chest': Item("empty chest", "old broken treasure chest"),
    'hidden coins': Item("hidden coins", "hiding in a small hole in the wall, is a few more dusty gold medalians")
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

# Link items to rooms

room['outside'].items_list = [item['sword'], item['rocks']]
room['foyer'].items_list = [item['rocks']]
room['overlook'].items_list = [item['rocks'], item['axe']]
room['narrow'].items_list = [item['rocks'], item['coins']]
room['treasure'].items_list = [item['empty chest'], item['hidden coins']]

def location(player, prev_room = ''):
    if player.room.enter_room != prev_room:
        print(f"\nPlayer is in room: {player.room.name} \n{player.room.description}\nItems in this room:")
        for item in player.room.items_list:
            print(item.name)
#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player('Sydney', room['outside'], [])
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

direction = {
    'n': 'n_to',
    'e': 'e_to',
    's': 's_to',
    'w': 'w_to',
}

location(player)

while True:

    cmd = input('\n n/e/s/w -> \n')
    words = cmd.split(' ')

    # if cmd == 'n' and hasattr(player.room, 'n_to'):
    #     player.room = player.room.n_to
    # elif cmd == 'e' and hasattr(player.room, 'e_to'):
    #     player.room = player.room.e_to
    # elif cmd == 's' and hasattr(player.room, 's_to'):
    #     player.room = player.room.s_to
    # elif cmd == 'w' and hasattr(player.room, 'w_to'):
    #     player.room = player.room.w_to
    # elif cmd == 'q':
    #     break
    # else:
    #     print('\n Invalid command \n')

    if direction.get(cmd):
        prev_room = player.room.name
        player.room = player.room.enter_room(direction[cmd])
        location(player, prev_room)
    elif words[0] == 'take' and item.get(words[1]):
        player.take(item.get(words[1]))
    elif words[0] == 'drop' and item.get(words[1]):
        player.drop(item.get(words[1]))
    elif cmd == 'q':
        break
    else:
        print('\n Invalid command \n')
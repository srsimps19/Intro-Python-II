# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, room, inventory):
        self.name = name
        self.room = room 
        self.inventory = inventory
    def take():
        if item in self.room.items_list:
            self.room.items_list.remove(item)
            self.inventory.append(item)
        else:
            print("That object is not in this room!")
    def drop():
        if item in self.inventory:
            self.inventory.remove(item)
            self.room.items_list.append(item)
        else:
            print("You don't have that item in your inventory!")
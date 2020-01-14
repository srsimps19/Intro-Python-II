# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description 
        self.n_to = self
        self.e_to = self
        self.s_to = self
        self.w_to = self
    def enter_room(self, direction):
        new_room = self.__getattribute__(direction)

        if new_room == self:
            print("You can't move that direction")
        return new_room

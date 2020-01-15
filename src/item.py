class Item:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc 
    def on_take(self):
        print(f"You have picked up {self.name}.")
    def on_drop(self):
        print(f"You have dropped {self.name}.")

class LightSource(Item):
    def __init__(self, name, desc):
        super().__init__(name, desc)
        self.name = name
    def on_drop(self):
        print("It is not wise to drop your source of light!")
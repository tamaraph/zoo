from animal import Animal

class Bear(Animal):

    def __init__(self, name, age, race, health=0, happiness=0):
        super().__init__(name, age, health, happiness)
        self.race = race
class Zoo:

    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    def add_animal(self, new_animal):
        for animal in self.animals:
            if animal.name == new_animal.name:
                return False
        self.animals.append(new_animal)
        return True
        
    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            print(animal.display_info())

""" class animal:
    def __init__(self, name, age, gender , health, happiness, feed ,display_info):
        self.name = name
        self.age = age
        self.gender = gender
        self.health = health
        self.happiness = happiness
        self.feed = feed
        self.display_info = display_info """

""" zoo1 = Zoo("John's Zoo")
zoo1.add_lion("Nala")
zoo1.add_lion("Simba")
zoo1.add_tiger("Rajah")
zoo1.add_tiger("Shere Khan")
zoo1.print_all_info() """
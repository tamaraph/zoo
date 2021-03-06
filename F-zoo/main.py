from zoo import Zoo
from animal import Animal
from lion import Lion
from tiger import Tiger
from bear import Bear
import os

def menu(): 
    option = -1
    while option < 0 or option > 3:
        os.system("cls")
        print("Menu: Central's Zoo")
        print("[1] Add Animal")
        print("[2] Feed all Animals")
        print("[3] Show all Animals")
        print("[0] Exit")
        try:
            option = int(input("Choice an option: "))
        except:
            input("Need a numeric option")
        if option < 0 or option > 3:
            input("Press ENTER to continue")
    return option

######################################################################################
option = menu()
zoo1 = Zoo("Central's Zoo")

while option > 0:
    if option == 1:
        print("Input new data option: ")
        animal_type = int(input("Type of animal: (1) Lion (2) Bear (3) Tiger: "))
        if animal_type == 1:
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            color = input("The color of the Lion is Brown (Yes / No): ")
            if color == "Yes" or color == "yes" or color == "Y" or color == "y" or color == "YES":
                color = "Brown"
            else:
                color = "Yellow"
            new_animal = Lion(name, age, color, health=10, happiness=10)
        
        elif animal_type == 2:
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            race = input("The race of the Bear if a Polar Bear? (Yes / No): ")
            if race == "Yes" or race == "yes" or race == "Y" or race == "y" or race == "YES":
                race = "Polar"
            else:
                race = "Grizzle"
            new_animal = Bear(name, age, race, health=15, happiness=15)

        elif animal_type == 3:
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            gender = input("The gender of the Tiger is male? (Yes / No): ")
            if gender == "Yes" or gender == "yes" or gender == "Y" or gender == "y" or gender == "YES":
                gender = "Male"
            else:
                gender = "Female"
            new_animal = Tiger(name, age, gender, health=15, happiness=20)

        if zoo1.add_animal(new_animal) == True:
            print("Congratulations animal added")
            zoo1.print_all_info()
        else:
            print("System failed to add animal")
    
    elif option == 2:
        #print("Ingrese los datos del animal a alimentar: ")
        animal_type = input("Do you want to feed all animals? (Yes / No):")
        if animal_type == "Yes" or animal_type == "yes" or animal_type == "Y" or animal_type == "y" or animal_type == "YES":
            for i in range(len(zoo1.animals)):
                Lion.feed(zoo1.animals[i])
        else:
            print("The animals were not feed")
    
    elif option == 3:
        print("The animals admitted are:")
        zoo1.print_all_info()
    
    input("Press ENTER to continue")
    option = menu()
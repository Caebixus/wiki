# When we use a class we name the resulting objects instances.
# When we change resulting object (instance) that instance is responsible, not the class itself
# Methods are functions but belong to the class

class Animal:
    def __init__(self, fur_color):
        self.fur_color = fur_color

    def speak(self):
        print("Raawwwrr")

    def eat(self):
        print("I'm eating meat")

    def chase(self, animal):
        print(animal, "- should we chase?")

    def get_fur_color(self):
        print("Getting fur color:", self.fur_color)

class HouseCat(Animal):

    def __init__(self, fur_color):
        super().__init__(fur_color)
        print("Fur color was saved")

    def eat(self):
        super().eat()
        print("Also fish")

    def chase(self, animal):
        super().chase(animal)
        print("Yes, lets do this and hunt down", animal)

house_cat = HouseCat("Orange")
house_cat.get_fur_color()


# Python is an object oriented programming language.
# Almost everything in Python is an object, with its properties and methods.
# A Class is like an object constructor, or a "blueprint" for creating objects.

# super()method -> execute the method above class as well

# dunder method -> __init__(self)
# this means execute this before everything else in class. We can overwrite it, use Super() on it
# dog class exercises

class Dog:
    species = "Canis familiaris"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound="Woof!"):
        return f"{self.name} says {sound}"

inu = Dog("Inu", 7)
poppy = Dog("Poppy", 12)


class Car:
    def __init__(self,colour,mileage):
        self.colour = colour
        self.mileage = mileage
    def __str__(self):
        return f"{self.colour} car has {self.mileage} miles"


bluecar = Car("Blue",20000)
redcar = Car("Red",30000)
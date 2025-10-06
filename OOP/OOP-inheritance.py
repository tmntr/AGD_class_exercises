class Dog(object):
    species = "Canis familiaris"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound="Woof!"):
        return f"{self.name} says {sound}"

class Dachsund(Dog):
    def speak(self,sound = "Arf! Arf!"):
        return super().speak(sound)

rufus = Dachsund("Rufus", 25)




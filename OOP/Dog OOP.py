# dog class exercises

class Dog:
    def __init__(self,dname,dbreed,dage):
        self.name=dname
        self.breed=dbreed
        self.age=dage
        self.isgoodboy = True
        self.isgoodgirl = True
    def birthday(self):
        self.age += 1
    def here_doggy(self,usedname):
        if usedname==self.name:
            if self.isgoodboy or self.isgoodgirl:
                self.respond()
            else:
                self.speak()
    def respond(self):
        print("WOOF! (I'm on my way!)")
    def speak(self):
        return f"{self.name} says 'Woof'"


inu = Dog('Inu','cockapoo',7)
poppy = Dog('Poppy','labrador',7)

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
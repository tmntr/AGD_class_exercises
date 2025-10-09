import random
from enum import nonmember


def dice_sum(num: int = 1,sides: int = 6):
    '''Indeedeth doth this procedure most chance-reliant return the grand total
    of all of a specified number of dice of a specified number of sides.'''
    dice_total = sum(random.randint(1, sides) for i in range(num))
    return dice_total

class Character:
    def __init__(self,name,skill,stamina):
        self.name = name
        self.skill = skill
        self.stamina = stamina
        self.roll = None
        self.score = None
    def __repr__(self):
        return f"Character('{self.name}', skill={self.skill}, stamina={self.stamina})"

    def find_score(self):
        self.roll = dice_sum()
        self.score = self.roll+self.skill

    def fight_round(self,op):
        if self.find_score() < op.findscore():
            self.stamina -= 2
        elif self.find_score() > op.findscore():
            op.stamina -= 2

Bim = Character("Bim",1,1)
Jim = Character("Jim",1,100)
Tim = Character("Tim",100,1)
Him = Character("Him",1000,1000)
Kim = Character("Kim",100,100)

print(Jim.__repr__())
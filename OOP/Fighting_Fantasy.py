import random
from enum import nonmember


def battle(p1,p2):
    while not(p1.is_dead or p2.is_dead):
        p1.fight_round(p2)
        print(p1.stamina, p2.stamina)

    if p1.stamina > p2.stamina:
        print(f"{p1.name} wins!")
    elif p2.stamina > p1.stamina:
        print(f"{p2.name} wins!")
    else:
        print("A draw.")

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


    def take_hit(self,damage = 2):
        self.stamina -= damage

    def fight_round(self,op):
        self.find_score()
        op.find_score()

        if self.score < op.score:
            self.take_hit()
        elif self.score > op.score:
            op.take_hit()
        else:
            self.take_hit(1)
            op.take_hit(1)

    def return_rolls_status(self):
        return(f"{self.name} rolled a {self.roll} for a total score of {self.score}")

    @property
    def is_dead(self):
        return self.stamina <= 0

    @is_dead.setter
    def is_dead(self,dead:bool):
        if dead:
            self.stamina = 0
        else:
            self.stamina = max(self.stamina,1)

class PlayerCharacter(Character):
    def __init__(self,name,skill,stamina,luck):
        super().__init__(name,skill,stamina)
        self.luck = luck

    @classmethod
    def generate_player_character(cls,name):
        skill = 6 + dice_sum(1,6)
        stamina = 12+dice_sum(2,6)
        luck = 12 + dice_sum(1,6)
        return cls(name,skill,stamina,luck)



Jim = Character("Jim",1,5)
Tim = Character("Tim",5,1)
Him = Character("Him",50,50)
Kim = Character("Kim",5,5)

Bim = PlayerCharacter("Bim",1,1,100)

characters = [Bim,Jim,Tim,Him,Kim]





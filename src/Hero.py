# import class
import random
from Character import Character

class Hero(Character):
    def __init__(self, name, health):
        super().__init__(name, health)

    # Attack hero
    @staticmethod
    def attack_hero(target):
        damage = random.randint(25, 30)
        target.health = target.health - damage
        return damage

    # Create Character
def create_hero():

    print(f"Create your Hero 🦸")
    name = input(f"Choose your name : ")
    health = random.randint(80, 100)
    # Création du hero
    hero1 = Hero(name, health)
    print(f"Your hero called {hero1.name} with a health {hero1.health} hp !")
    return hero1

# PV du hero
def hero_health(self):
    while self.health > 0:
        return sefl.health
    else:
        print(f"{hero.name} is dead")
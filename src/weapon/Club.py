# import les classes
import random

from src.weapon.Weapon import Weapon


class Club(Weapon):
    def __init__(self, name, damage, length, weight, health):
        # super() = héritage
        super().__init__(name, damage, length, weight, health)


    @staticmethod
    def create_club(defaultName):
        damage = random.randint(15,28)
        health = random.randint(90, 100)
        print(f"Create your weapon ⚔️")
        name = input(f"Choose your name : ")
        if not name:
            club1 = Club(defaultName, damage, 13, 90, health)
            print(f"Your weapon ⚔️ : {club1.name} between 12 and 28 damage, a weight of {club1.weight} Kg and a health of {club1.health} hp !")
            return club1            
        club1 = Club(name, damage, 13, 90, health)
        print(f"Your weapon ⚔️ : {club1.name} between 12 and 28 damage, a weight of {club1.weight} Kg and a health of {club1.health} hp !")
        return club1
# import les classes
import random
from Weapon import Weapon

class Club(Weapon):
    def __init__(self, name, damage, length, weight, health):
        # super() = héritage
        super().__init__(name, damage, length, weight, health)



    # Create club
    @staticmethod
    def create_club():
        print(f"Create your weapon ⚔️")
        name = input(f"Choose your name : ")
        return Club.create_club_n(name)

    @staticmethod
    def create_club_n(name):
        damage = random.randint(12,28)
        health = random.randint(90, 100)
        club1 = Club(name, damage, 13, 90, health)
        print(f"Your weapon ⚔️ : {club1.name} between 12 and 28 damage, a weight of {club1.weight} Kg and a health of {club1.health} hp !")
        return club1
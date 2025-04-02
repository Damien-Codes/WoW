# import les classes
import random

from src.weapon.Weapon import Weapon


class Sword(Weapon):
    def __init__(self, name, damage, length, weight, health):
        super().__init__(name, damage, length, weight, health)

    def create_sword(defaultName):
        damage = random.randint(15,28)
        health = random.randint(90, 100)
        print(f"Create your weapon ⚔️")
        name = input(f"Choose your name : ")
        if not name:
            sword1 = Sword(defaultName, damage, 90, 100, health)
            print(f"Your weapon ⚔️ : {sword1.name} between 12 and 28 damage, a weight of {sword1.weight} Kg and a health of {sword1.health} hp !")
            return sword1
        sword1 = Sword(name, damage, 90, 100, health)
        print(f"Your weapon ⚔️ : {sword1.name} between 12 and 28 damage, a weight of {sword1.weight} Kg and a health of {sword1.health} hp !")
        return sword1
# import les classes
import random
from Weapon import Weapon

class Sword(Weapon):
    def __init__(self, name, damage, length, weight, health):
        super().__init__(name, damage, length, weight, health)

# Création d'une epee
def create_sword():
    name = input("choisir le nom de l'équipement : ")
    damage = random.randint(12,28)
    health = random.randint(90, 100)
    sword1 = Sword(name, damage, 90, 100, health)
    print("Votre équipement  :", sword1.name + " qui fais entre 12 et 28 dégats, un poids de ", str(sword1.weight) + " Kg et une vie de ", str(sword1.health) + " pv !")
    return sword1
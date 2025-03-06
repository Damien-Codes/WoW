# import les classes
import random
from Weapon import Weapon

class Club(Weapon):
    def __init__(self, name, damage, length, weight, health):
        # super() = héritage
        super().__init__(name, damage, length, weight, health)



# Création d'un gourdin
def create_club():
    print("Création de l'équipement du monstre ◘ : ")
    name = input("choisir le nom de l'équipement : ")
    damage = random.randint(12,28)
    health = random.randint(90, 100)
    club1 = Club(name, damage, 13, 90, health)
    print("Votre équipement  :", club1.name + " qui fais entre 12 et 28 dégats, un poids de ", str(club1.weight) + " Kg et une vie de ", str(club1.health) + " pv !")
    return club1
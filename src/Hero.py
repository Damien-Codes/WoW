# import class
import random
from Person import Person

class Hero(Person):
    def __init__(self, name, health):
        super().__init__(name, health)



    # attack hero
    @staticmethod
    def attack_hero(target):
        damage = random.randint(25, 30)
        target.health = target.health - damage
        return damage



    # Création de personnage
def create_hero():

    print("Création de votre héro ╬")
    name = input("Création du nom de votre hero : ")
    health = random.randint(80, 100)
    # Création du hero
    hero1 = Hero(name, health)
    print("Votre héros s'appelle désormais", hero1.name + " avec une vie de ", str(hero1.health) + " pv !")
    return hero1

# PV du hero
def hero_health(self):
    #print(f"{self.nom} a actuellement {self.vie} PV.")
    while self.health > 0:
        return sefl.health
    else:
        print("Le Héro est dead")



#def attaque()
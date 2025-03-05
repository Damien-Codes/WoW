# import les classes
import random
from Person import Person

class Hero(Person):
    def __init__(self,nom, prenom, vie):
        super().__init__(nom, prenom, vie)

    # Création de personnage
def create_hero():

    print("Création de votre héro ╬")
    nom = input("Choisir le nom de votre hero : ")
    prenom = input("Choisir le prénom de votre hero : ")
    # Création du hero
    hero1 = Hero(nom, prenom, random.randint(80, 100))
    print("Votre héros s'appelle désormais", hero1.nom, hero1.prenom + " avec une vie de ", str(hero1.vie) + " pv !")
    return hero1

# PV du hero
def life_hero(self):
    return self.vie > 0

# attaque du hero
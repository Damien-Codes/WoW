# import les classes
import random
from Person import Person

class Hero(Person):
    def __init__(self,nom, vie):
        super().__init__(nom, vie)

    # Getteurs
    def get_nom(self):
        return self.nom

    def get_vie(self):
        return self.vie

    # Setteur
    def set_nom(self, nouveau_nom):
        if isinstance(nouveau_nom, str) and len(nouveau_nom) > 0:
            self.nom = nouveau_nom
        else:
            print("Erreur : Le nom doit être une chaîne de caractères non vide.")

    def set_vie(self, nouvelle_vie):
        if nouvelle_vie >= 0:
            self.vie = nouvelle_vie
        else:
            self.vie = 0

    # attaque du hero
    def attack_hero(self, cible):
        degats = random.randint(5, 10)
        cible.set_vie(cible.get_vie() - degats)
        return degats



    # Création de personnage
def create_hero():

    print("Création de votre héro ╬")
    nom = input("Création du nom de votre hero : ")
    vie = random.randint(80, 100)
    # Création du hero
    hero1 = Hero(nom, vie)
    print("Votre héros s'appelle désormais", hero1.nom + " avec une vie de ", str(hero1.vie) + " pv !")
    return hero1

# PV du hero
def life_hero(self):
    #print(f"{self.nom} a actuellement {self.vie} PV.")
    return self.vie



#def attaque()
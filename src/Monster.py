# import les classes
import random
from Person import Person


class Monster(Person):
    def __init__(self,nom, prenom, vie):
        super().__init__(nom, prenom, vie)

    # Création de monster
def create_monster():
    print("Création de votre monstre ╬")
    nom = input("choisir le nom de votre monstre : ")
    prenom = input("choisir le prenom de votre monstre : ")
    # Création du monstre
    monstre1 = Monster(nom, prenom, random.randint(80, 100))
    print("Votre monstre s'appelle désormais", monstre1.nom, monstre1.prenom + " avec une vie de ", str(monstre1.vie) + " pv !")
    return monstre1
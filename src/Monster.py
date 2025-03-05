# import les classes
import random
from Person import Person


class Monster(Person):
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

    def set_vie(self, nouvelle_vie):
        if nouvelle_vie >= 0:
            self.vie = nouvelle_vie
        else:
            self.vie = 0  # ✅ Empêche la vie d'être négative

    # attaque du monstre
    def attack_monstre(self, cible):
        degats = random.randint(5, 10)
        cible.set_vie(cible.get_vie() - degats)
        return degats

    # Création de monster
def create_monster():
    print("Création de votre monstre ╬")
    nom = input("Création du nom de votre monstre : ")
    vie = random.randint(80, 100)
    # Création du monstre
    monstre1 = Monster(nom, vie)
    print("Votre monstre s'appelle désormais", monstre1.nom + " avec une vie de ", str(monstre1.vie) + " pv !")
    return monstre1
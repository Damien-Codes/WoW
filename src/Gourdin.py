# import les classes
import random
from Weapon import Weapon

class Gourdin(Weapon):
    def __init__(self, nom, degats, poids, vie):
        # super() = héritage
        super().__init__(nom, degats, poids, vie)

    # Getteurs
    def get_nom(self):
        return self.nom

    def get_poids(self):
        return self.poids

    def vie(self):
        return self.vie

    # Setteur
    def set_nom(self, nouveau_nom):
        if isinstance(nouveau_nom, str) and len(nouveau_nom) > 0:
            self.nom = nouveau_nom
        else:
            print("Erreur : Le nom doit être une chaîne de caractères non vide.")

    def set_vie(self, nouvelle_vie):
        if isinstance(nouvelle_vie, str) and len(nouvelle_vie) > 0:
            self.vie = nouvelle_vie
        else:
            print("Erreur : Le nom doit être une chaîne de caractères non vide.")

# Création d'un gourdin
def creation_gourdin():
    print("Création de l'équipement du monstre ◘ : ")
    nom = input("choisir le nom de l'équipement : ")
    degats = random.randint(12,28)
    gourdin1 = Gourdin(nom, degats, 90, 100)
    print("Votre équipement  :", gourdin1.nom +" qui fais entre 12 et 28 dégats, un poids de ", str(gourdin1.poids) +" Kg et une vie de ", str(gourdin1.vie) + " pv !")
    return gourdin1
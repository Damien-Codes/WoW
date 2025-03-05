import random

class Weapon:
    def __init__(self, id, nom, degats, longueur, poids, vie):
        self.id = id
        self.nom = nom
        self.degats = degats
        self.longueur = longueur
        self.poids = poids
        self.vie = vie

class Gourdin(Weapon):
    def __init__(self, id, nom, degats, longueur, poids, vie):
        # super() = héritage
        super().__init__(id, nom, degats, longueur, poids, vie)

class Epee(Weapon):
    def __init__(self, id, nom, degats, longueur, poids, vie):
        super().__init__(id, nom, degats, longueur, poids, vie)

# Création d'une epee
def creation_epee():
    print("Création de l'équipement du hero ◘ : ")
    nom = input("choisir le nom de l'équipement : ")
    epee1 = Epee(1, nom, random.randint(12,28), 90, 15, 100)
    print("Votre équipement  :", epee1.nom +" qui fais entre 12 et 28 dégats avec une longueur de", str(epee1.longueur) +" cm, un poids de ", str(epee1.poids) +" Kg et une vie de ", str(epee1.vie) + " pv !")
    return epee1

# Création d'un gourdin
def creation_gourdin():
    print("Création de l'équipement du monstre ◘ : ")
    nom = input("choisir le nom de l'équipement : ")
    gourdin1 = Gourdin(1, nom, random.randint(12,28), 90, 15, 100)
    print("Votre équipement  :", gourdin1.nom +" qui fais entre 12 et 28 dégats avec une longueur de", str(gourdin1.longueur) +" cm, un poids de ", str(gourdin1.poids) +" Kg et une vie de ", str(gourdin1.vie) + " pv !")
    return gourdin1
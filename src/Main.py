# Importation des classes et les methodes

from Hero import create_hero
from Monster import create_monster
from Weapon import creation_epee, creation_gourdin

class Jeu:
    # Commencer la partie
    def commencer_partie(self):
        commencer = input("Voulez commencer a jouer ? (o/n) : ").lower()
        if commencer.lower() == "o":
            # Création de personnage et de l'équipement

            hero = create_hero()
            epee = creation_epee()
            monstre = create_monster()
            gourdin = creation_gourdin()
            print("Début du combat : ", hero.prenom + " utilise ", epee.nom + " comme office d'arme contre", monstre.prenom + " utilise ", gourdin.nom + " comme office d'arme.")
            print("Hero :", hero.prenom + " | vie :", str(hero.vie) + " restant")
            print("Monstre :", monstre.prenom + " | vie :", str(monstre.vie) + " restant")
            print("Au tours de", hero.prenom+ " d'attaquer")
            #hero.attaquer(monstre, epee)
            #print("Il reste ", str(monstre.vie) + "PV à" , monstre.prenom)
            #monstre.attaquer(hero, gourdin)
            #print("Il reste ", str(hero.vie) + "PV à" , hero.prenom)
        else:
            print("A bientôt !")


# Lancer le jeu
jeu = Jeu()
jeu.commencer_partie()
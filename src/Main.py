# Importation des classes et les methodes

from Hero import create_hero
from Monster import create_monster
from Gourdin import creation_gourdin
from Epee import creation_epee


class Jeu:
    # Commencer la partie
    @staticmethod
    def commence_parte():
        # Création de personnage et de l'équipement

        hero = create_hero()
        epee = creation_epee()
        monstre = create_monster()
        gourdin = creation_gourdin()

        print("Début du combat : ", hero.get_nom() + " utilise ", epee.get_nom() + " comme office d'arme contre", monstre.get_nom() + " utilise ", gourdin.get_nom() + " comme office d'arme.")
        print("| -------------------------------|")
        print("| Hero :", hero.get_nom() + " | vie :", str(hero.get_vie()) + " restant |")
        print("| Monstre :", monstre.get_nom() + " | vie :", str(monstre.get_vie()) + " restant |")
        print("| -------------------------------|")

        print("Au tours de", hero.get_nom() + " d'attaquer")


#Round 1
        # Attaque du Hero
        print(f"{hero.get_nom()} inflige {hero.attack_hero(monstre)} dégâts a {monstre.get_nom()}")
        print(f"Le monstre lui reste  {monstre.get_vie()} vie")
        # Attaque du monstre
        print(f"{monstre.get_nom()} inflige {monstre.attack_monstre(hero)} dégâts a {hero.get_nom()}")
        print(f"Le hero lui reste  {hero.get_vie()} vie")

#Round 2
        # Attaque du Hero
        print(f"{hero.get_nom()} inflige {hero.attack_hero(monstre)} dégâts a {monstre.get_nom()}")
        print(f"Le monstre lui reste  {monstre.get_vie()} vie")
        # Attaque du monstre
        print(f"{monstre.get_nom()} inflige {monstre.attack_monstre(hero)} dégâts a {hero.get_nom()}")
        print(f"Le hero lui reste  {hero.get_vie()} vie")



        #print(str(hero.get_vie()))
        #print(str(monstre.get_vie()))
        #print(monstre.get_vie() - degatshero)
        #print("Vie du monstre ", monstre.get_vie())
        #print(hero.get_vie() - attack_hero())

        #print(attack_hero)


        #hero.attaquer(monstre, epee)
        #print("Il reste ", str(monstre.vie) + "PV à" , monstre.prenom)
        #monstre.attaquer(hero, gourdin)
        #print("Il reste ", str(hero.vie) + "PV à" , hero.prenom)


# Lancer le jeu
jeu = Jeu()
jeu.commence_parte()
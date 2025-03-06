# Import class and methods

from Hero import create_hero
from Monster import create_monster
from Club import create_club
from Sword import create_sword


class Game:
    # start game
    @staticmethod
    def start_game():
        # Création de personnage et de l'équipement

        hero = create_hero()
        epee = create_sword()
        monstre = create_monster()
        gourdin = create_club()

        print("Début du combat : ", hero.name + " utilise ", epee.name + " comme office d'arme contre", monstre.name + " utilise ", gourdin.name + " comme office d'arme.")
        print("| -------------------------------|")
        print("| Hero :", hero.name + " | vie :", str(hero.health) + " restant |")
        print("| Monstre :", monstre.name + " | vie :", str(monstre.health) + " restant |")
        print("| -------------------------------|")

        print("Au tours de", hero.name + " d'attaquer")


#Round 1
        # Attaque du Hero
        print(f"{hero.name} inflige {hero.attack_hero(monstre)} dégâts a {monstre.name}")
        print(f"Le monstre lui reste  {monstre.health} vie")
        # Attaque du monstre
        print(f"{monstre.name} inflige {monstre.attack_monster(hero)} dégâts a {hero.name}")
        print(f"Le hero lui reste  {hero.health} vie")

#Round 2
        # Attaque du Hero
        print(f"{hero.name} inflige {hero.attack_hero(monstre)} dégâts a {monstre.name}")
        print(f"Le monstre lui reste  {monstre.health} vie")
        # Attaque du monstre
        print(f"{monstre.name} inflige {monstre.attack_monster(hero)} dégâts a {hero.name}")
        print(f"Le hero lui reste  {hero.health} vie")

        #Round 3
        # Attaque du Hero
        print(f"{hero.name} inflige {hero.attack_hero(monstre)} dégâts a {monstre.name}")
        print(f"Le monstre lui reste  {monstre.health} vie")
        # Attaque du monstre
        print(f"{monstre.name} inflige {monstre.attack_monster(hero)} dégâts a {hero.name}")
        print(f"Le hero lui reste  {hero.health} vie")

        #Round 4
        # Attaque du Hero
        print(f"{hero.name} inflige {hero.attack_hero(monstre)} dégâts a {monstre.name}")
        print(f"Le monstre lui reste  {monstre.health} vie")
        # Attaque du monstre
        print(f"{monstre.name} inflige {monstre.attack_monster(hero)} dégâts a {hero.name}")
        print(f"Le hero lui reste  {hero.health} vie")

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
game = Game()
game.start_game()
# Import class and methods
from src.Club import Club
from src.Hero import Hero
from src.Monster import Monster
from src.Sword import Sword


class Game:
    @staticmethod
    def fight(hero, monster):
        while True:
            # Le héros attaque
            damage_hero = hero.attack(monster)
            print(f"{hero.name} inflige {damage_hero} dégâts à {monster.name}.")

            if not monster.isAlive():
                break  # Fin du combat

            # Le monstre attaque
            damage_monster = monster.attack(hero)
            print(f"{monster.name} inflige {damage_monster} dégâts à {hero.name}.")

            if not hero.isAlive():
                break  # Fin du combat

        if monster.isAlive():
            print(f"{hero.name} est mort ! {monster.name} a gagné ! 💀")
        if hero.isAlive():
            print(f"{monster.name} est mort ! {hero.name} a gagné ! 💀")

    # start gamea
    @staticmethod
    def start_game():
        # Create Character and weapon
        hero = Hero.create_hero_n("toto")
        sword = Sword.create_sword_n("ttt")
        monster = Monster.create_monster_n("Bob")
        club = Club.create_club_n("rrrrr")

        print(f"Start fight : {hero.name} used {sword.name} against {monster.name} used {club.name}")
        print(f"| -------------------------------|")
        print(f"| Hero : {hero.name} | Health : {hero.health} |")
        print(f"| Monster : {monster.name} | Health : {monster.health} |")
        print(f"| -------------------------------|")

        print(f"{hero.name} attacks first !") # make a random function for starting turn between hero and monster

        Game.fight(hero, monster)




# Lancer le jeu
Game.start_game()
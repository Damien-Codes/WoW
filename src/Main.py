# Import class and methods

from Hero import create_hero
from Monster import create_monster
from Club import create_club
from Sword import create_sword


class Game:
    # start game
    @staticmethod
    def start_game():
        # Create Character and weapon

        hero = create_hero()
        sword = create_sword()
        monster = create_monster()
        club = create_club()

        print(f"Start fight : {hero.name} used {sword.name} against {monster.name} used {club.name}")
        print(f"| -------------------------------|")
        print(f"| Hero : {hero.name} | Health : {hero.health} |")
        print(f"| Monster : {monster.name} | Health : {monster.health} |")
        print(f"| -------------------------------|")

        print(f"{hero.name} attacks first !") # make a random function for starting turn between hero and monster


#Round 1
        # Attack hero
        print(f"{hero.name} inflicted {hero.attack_hero(monster)} damage at {monster.name}")
        print(f"The monster remains {monster.health} health")
        # Attack monster
        print(f"{monster.name} inflicted {monster.attack_monster(hero)} damage at {hero.name}")
        print(f"The monster remains {hero.health} health")

#Round 2
        # Attack hero
        print(f"{hero.name} inflicted {hero.attack_hero(monster)} damage at {monster.name}")
        print(f"The monster remains {monster.health} health")
        # Attack monster
        print(f"{monster.name} inflicted {monster.attack_monster(hero)} damage at {hero.name}")
        print(f"The monster remains {hero.health} health")

        #Round 3
        # Attack hero
        print(f"{hero.name} inflicted {hero.attack_hero(monster)} damage at {monster.name}")
        print(f"The monster remains {monster.health} health")
        # Attack monster
        print(f"{monster.name} inflicted {monster.attack_monster(hero)} damage at {hero.name}")
        print(f"The monster remains {hero.health} health")


# Lancer le jeu
game = Game()
game.start_game()
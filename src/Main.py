import random
from Club import Club
from Hero import Hero
from Monster import Monster
from Sword import Sword
from Character import Character

class Game:
       
    @staticmethod
    def start_game():
        hero = Hero.create_hero("Trump")
        sword = Sword.create_sword("Epee")
        monster = Monster.create_monster("Macron")
        club = Club.create_club("Gourdin")

        print(f"Start fight : {hero.name} used {sword.name} against {monster.name} used {club.name}")
        print(f"| -------------------------------|")
        print(f"| Hero : {hero.name} | Health : {hero.health} |")
        print(f"| Monster : {monster.name} | Health : {monster.health} |")
        print(f"| -------------------------------|")

        Character.fight(hero, monster)

# Start the game
Game.start_game()
# import
import random

from Club import Club
from Hero import Hero
from Monster import Monster
from Sword import Sword
from Character import Character
from Food import Food
from Shield import Shield


class Game:
       
    @staticmethod
    def start_game():
        # Create Hero
        hero = Hero.create_hero("Trump")
        # Add a Sword to bag
        sword = Sword.create_sword("Epee")
        hero.bag.add_weapon(sword)
        # Add a Shield to bag
        shields = Shield.create_shield()
        for shield_h in shields:
            hero.bag.add_shield(shield_h)
        # Add a Food to bag
        foods = Food.create_food()
        for food_h in foods:
            hero.bag.add_food(food_h)
        # Display the Hero bag
        print(hero.bag)

        # Create Monster
        monster = Monster.create_monster("Macron")
        # Add a Sword to bag
        club = Club.create_club("Gourdin")
        monster.bag.add_weapon(club)
        # Add a Shield to bag
        shields = Shield.create_shield()  # Liste de 0, 1 ou plusieurs boucliers
        for shield_m in shields:
            monster.bag.add_shield(shield_m)
        # Add a Food to bag
        foods = Food.create_food()
        for food_m in foods:
            monster.bag.add_food(food_m)
        # Display the Monster bag
        print (monster.bag)

        print(f"Start fight : {hero.name} used {hero.bag.weapon.name} against {monster.name} used {monster.bag.weapon.name}")
        print(f"| --------------------------------------------- |")
        print(f"| Hero : {hero.name} | Health : {hero.health} | Stamina : {hero.stamina} |")
        print(f"| Monster : {monster.name} | Health : {monster.health} | Stamina : {monster.stamina} |")
        print(f"| --------------------------------------------- |")


        Character.fight(hero, monster)



        print(hero.bag)
        print(monster.bag)


        # display the Food
        #Food.create_food()
        # display the shield
        #shields = Shield.create_shield()
        #for shield in shields:
        #    print(shield)

# Start the game
Game.start_game()
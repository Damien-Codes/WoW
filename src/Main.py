#import
from src.char.Character import Character
from src.char.Hero import Hero
from src.char.Monster import Monster
from src.stack.Food import Food
from src.stack.Shield import Shield
from src.weapon.Club import Club
from src.weapon.Sword import Sword


class Game:

    @staticmethod
    def start_game():
        # Create Hero
        hero = Hero.create_hero("Trump")

        # Add a Sword to Inventory
        sword = Sword.create_sword("Epee")
        hero.Inventory.add_weapon(sword)

        # Add a Shield to Inventory
        shields = Shield.create_shield()
        for shield_h in shields:
            hero.Inventory.add_shield(shield_h)

        # Add a Food to Inventory
        foods = Food.create_food()
        for food_h in foods:
            hero.Inventory.add_food(food_h)

        # Display the Hero Inventory
        print(hero.Inventory)

        # Create Monste
        monster = Monster.create_monster("Macron")

        # Add a Club to Inventory
        club = Club.create_club("Gourdin")
        monster.Inventory.add_weapon(club)

        # Add a Shield to Inventory
        shields = Shield.create_shield()
        for shield_m in shields:
            monster.Inventory.add_shield(shield_m)

        # Add a Food to Inventory
        foods = Food.create_food()
        for food_m in foods:
            monster.Inventory.add_food(food_m)

        # Display the Monster Inventory
        print(monster.Inventory)

        print(f"Start fight: {hero.name} used {hero.Inventory.weapon.name} against {monster.name} using {monster.Inventory.weapon.name}")
        print(f"| --------------------------------------------- |")
        print(f"| Hero : {hero.name} | Health : {hero.health} | Stamina : {hero.stamina} |")
        print(f"| Monster : {monster.name} | Health : {monster.health} | Stamina : {monster.stamina} |")
        print(f"| --------------------------------------------- |")

        Character.fight(hero, monster)

        print(hero.Inventory)
        print(monster.Inventory)

# Start the game
Game.start_game()

# import
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
        hero.inventory.add_weapon(sword)

        # Add a Shield to Inventory
        shields = Shield.create_shield()
        for shield_h in shields:
            hero.inventory.add_shield(shield_h)

        # Add Food to Inventory
        foods = Food.create_food()
        for food_h in foods:
            hero.inventory.add_food(food_h)

        # Display Hero's Inventory
        print(hero.inventory)

        # Create Monster
        monster = Monster.create_monster("Macron")

        # Add a Club to Inventory
        club = Club.create_club("Gourdin")
        monster.inventory.add_weapon(club)

        # Add a Shield to Inventory
        shields = Shield.create_shield()
        for shield_m in shields:
            monster.inventory.add_shield(shield_m)

        # Add Food to Inventory
        foods = Food.create_food()
        for food_m in foods:
            monster.inventory.add_food(food_m)

        # Display Monster's Inventory
        print(monster.inventory)

        print(f"Start fight: {hero.name} used {hero.inventory.weapon.name} against {monster.name} using {monster.inventory.weapon.name}")
        print(f"| --------------------------------------------- |")
        print(f"| Hero : {hero.name} | Health : {hero.health} | Stamina : {hero.stamina} | Shield : {hero.shield} |")
        print(f"| Monster : {monster.name} | Health : {monster.health} | Stamina : {monster.stamina} | Shield : {monster.shield} |")
        print(f"| --------------------------------------------- |")

        Character.fight(hero, monster)

        print(hero.inventory)
        print(monster.inventory)

# Start the game
Game.start_game()

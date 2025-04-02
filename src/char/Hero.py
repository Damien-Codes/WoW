# import class
import random

from src.char.Character import Character


class Hero(Character):
    def __init__(self, name, health, stamina, shield, foods):
        super().__init__(name, health, stamina, shield, foods)


    def create_hero(defaultName):
        print(f"Create your Hero 🦸")
        name = input(f"Choose your name : ")
        health = random.randint(80, 100)
        stamina = random.randint(20, 25)
        shield = random.randint(1, 5)
        foods = random.randint(1, 5)

        if not name:
            hero1 = Hero(defaultName, health, stamina, shield, foods)
            print(f"Your hero is called {hero1.name} with {hero1.health} HP and {hero1.stamina} of stamina.")
            return hero1
        # Create hero
        hero1 = Hero(name, health, stamina, shield, foods)
        print(f"Your hero is called {hero1.name} with {hero1.health} HP and {hero1.stamina} of stamina.")
        return hero1


    # health hero
    def hero_health(self):
        while self.health > 0:
            return self._health
        else:
            print(f"{Hero.name} is dead")
# import class
import random
from Character import Character

class Hero(Character):
    def __init__(self, name, health):
        super().__init__(name, health)


    def create_hero(defaultName):
        print(f"Create your Hero 🦸")
        name = input(f"Choose your name : ")
        health = random.randint(80, 100)
        if not name:
            hero1 = Hero(defaultName, health)
            print(f"Your hero called {hero1.name} with a health {hero1.health} hp !")
            return hero1
        # Create hero
        hero1 = Hero(name, health)
        print(f"Your hero called {hero1.name} with a health {hero1.health} hp !")
        return hero1

    # health hero
    def hero_health(self):
        while self.health > 0:
            return self._health
        else:
            print(f"{Hero.name} is dead")
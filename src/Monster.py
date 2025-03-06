# import class
import random
from Character import Character


class Monster(Character):
    def __init__(self, name, health):
        super().__init__(name, health)


        # Create monster
    @staticmethod
    def create_monster():
        print(f"Create your monster 🧌")
        name = input(f"Choose your name : ")
        return Monster.create_monster_n(name)

    @staticmethod
    def create_monster_n( name):
        health = random.randint(80, 100)
        monster1 = Monster(name, health)
        print(f"Your monster called {monster1.name} with a health {monster1.health}")
        return monster1
# import class
import random
from Character import Character


class Monster(Character):
    def __init__(self, name, health):
        super().__init__(name, health)


    # attack monster
    @staticmethod
    def attack_monster(target):
        damage = random.randint(5, 10)
        target.health = target.health - damage
        return damage

    # Create monster
def create_monster():
    print(f"Create your monster 🧌")
    name = input(f"Choose your name : ")
    health = random.randint(80, 100)
    monster1 = Monster(name, health)
    print(f"Your monster called {monster1.name} with a health {monster1.health}")
    return monster1
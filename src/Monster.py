# import class
import random
from Character import Character


class Monster(Character):
    def __init__(self, name, health):
        super().__init__(name, health)

    @staticmethod
    def create_monster(defaultName):
        print(f"Create your monster 🧌")
        name = input(f"Choose your name : ")
        health = random.randint(80, 100)
        if not name:
            monster1 = Monster(defaultName, health)
            print(f"Your monster called {monster1.name} with a health {monster1.health}")
            return monster1            
        monster1 = Monster(name, health)
        print(f"Your monster called {monster1.name} with a health {monster1.health}")
        return monster1
    
    # health monster
    def monster_health(self):
        while self.health > 0:
            return self._health
        else:
            print(f"{Monster.name} is dead")
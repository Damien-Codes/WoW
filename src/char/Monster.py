# import class
import random

from src.char.Character import Character


class Monster(Character):
    def __init__(self, name, health, stamina, shield, foods):
        super().__init__(name, health, stamina, shield, foods)

    def create_monster(defaultName):
        print(f"Create your monster 🧌")
        name = input(f"Choose your name : ")
        health = random.randint(80, 100)
        stamina = random.randint(20, 35)
        shield = random.randint(1, 5)
        foods = random.randint(1, 5)

        if not name:
            monster1 = Monster(defaultName, health, stamina, shield, foods)
            print(f"Your monster called {monster1.name} with {monster1.health} HP and {monster1.stamina} of stamina.")
            return monster1            
        monster1 = Monster(name, health, stamina, shield, foods)
        print(f"Your monster called {monster1.name} with {monster1.health} HP and {monster1.stamina} of stamina.")
        return monster1
    
    # health monster
    def monster_health(self):
        while self.health > 0:
            return self._health
        else:
            print(f"{Monster.name} is dead")
# import les classes
import random
from Weapon import Weapon

class Sword(Weapon):
    def __init__(self, name, damage, length, weight, health):
        super().__init__(name, damage, length, weight, health)

# Create sword
def create_sword():
    print(f"Create your weapon ⚔️")
    name = input(f"Choose your name : ")
    damage = random.randint(12,28)
    health = random.randint(90, 100)
    sword1 = Sword(name, damage, 90, 100, health)
    print(f"Your weapon ⚔️ : {sword1.name} between 12 and 28 damage, a weight of {sword1.weight} Kg and a health of {sword1.health} hp !")
    return sword1
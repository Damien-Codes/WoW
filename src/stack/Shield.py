# import class
import random
from src.stack.Inventory import Inventory

class Shield(Inventory):
    def __init__(self, name, weight, damageabsorption):
        super().__init__(name, weight)
        self.damageabsorption = damageabsorption

    def __str__(self):
        return f"{self.name} (absorbs {self.damageabsorption} damage, {self.weight}g)"

    # Method
    @staticmethod
    def create_shield():
        shields = [
            ("🛡️ Fer Shield", 650, 5),
            ("🛡️ Bronze shield", 600, 10),
            ("🛡️ Silver shield", 550, 15),
            ("🛡️ Gold shield", 500, 20),
            ("🛡️ Diamond shield", 450, 25),
        ]
        nb_shields = random.randint(0, 3)
        selected = random.sample(shields, nb_shields)
        shields = [Shield(name, weight, damageabsorption) for name, weight, damageabsorption in selected]
        return shields
# import class
import random
from src.stack.Inventory import Inventory

class Food(Inventory):
    def __init__(self, name, weight, stamina_gain):
        super().__init__(name, weight)
        self.stamina_gain = stamina_gain

    def __str__(self):
        return f"{self.name} (+{self.stamina_gain} stamina, {self.weight}g)"

    @staticmethod
    def create_food():
        foods = [
            ("🍏 Apple", 100, 10),
            ("🍇 Grapes", 80, 8),
            ("🥩 Meat", 200, 15),
            ("🍌 Bananas", 150, 12),
        ]
        nb_foods = random.randint(0, 3)
        selected = random.sample(foods, nb_foods)
        foods = [Food(name, weight, stamina_gain) for name, weight, stamina_gain in selected]
        return foods
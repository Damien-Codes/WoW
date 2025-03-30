# import class
import random
from Inventory import Inventory

class Food(Inventory):
    def __init__(self, name, weight, stamina_gain):
        super().__init__(name, weight)
        self.stamina_gain = stamina_gain

    def __str__(self):
        return f"{self.name} (+{self.stamina_gain} stamina, {self.weight}g)"

    @staticmethod
    def create_food():
        foods = [
            ("🍏 Pomme", 100, 10),
            ("🍇 Raisin", 80, 8),
            ("🥩 Viande", 200, 15),
            ("🍌 Bananes", 150, 12),
        ]
        nb_foods = random.randint(0, 3)
        selected = random.sample(foods, nb_foods)
        foods = [Food(name, weight, stamina_gain) for name, weight, stamina_gain in selected]
        return foods
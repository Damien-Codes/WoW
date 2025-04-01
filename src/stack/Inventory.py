#import
import random

class Inventory:
    def __init__(self, name="Inventaire", weight=0):
      self._name = name
      self._weight = weight

      # Inventory content
      self._weapon = None
      self._shields = []
      self._foods = []

    # Getters
    @property
    def name(self):
        return self._name

    @property
    def weight(self):
        return self._weight
    
    # Setters
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and len(new_name) > 0:
            self._name = new_name
        else:
            raise ValueError("Error : The name must be a non-empty string.")

    @weight.setter
    def weight(self, new_weight):
        self._weight = new_weight

    @property
    def weapon(self):
        return self._weapon

    @property
    def shields(self):
        return self._shields

    @property
    def foods(self):
        return self._foods

    # method
    def add_weapon(self, weapon):
        self._weapon = weapon

    def add_shield(self, shield):
        if isinstance(shield, list):
            self._shields.extend(shield)
        else:
            self._shields.append(shield)

    def add_food(self, food):
        if isinstance(food, list):
            self._foods.extend(food)
        else:
            self._foods.append(food)

    def __str__(self):
        shield_list = ", ".join(s.name for s in self.shields) or "None"
        food_list = ", ".join(f.name for f in self.foods) or "None"
        weapon_name = self.weapon.name if self.weapon else "None"
        return (
            f"🔪 Weapon : {weapon_name}\n"
            f"🛡️  Shields : {shield_list}\n"
            f"🍏 Foods : {food_list}"
        )
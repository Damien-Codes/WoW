# import
import random

class Character:
    def __init__(self, name, health):
        self._name = name
        self._health = health

    #Getters
    @property
    def name(self):
        return self._name
    @property
    def health(self):
        return self._health

    # Setters
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and len(new_name) > 0:
            self._name = new_name
        else:
            raise ValueError (f"Error : The name must be a non-empty string.")

    @health.setter
    def health(self, new_health):
        self._health = new_health

    def attack(self, target):
        damage = random.randint(25, 30) # TODO chercher l'arme ds inventory
        target.health -= damage
        return damage

    def isAlive(self):
        return self.health > 0
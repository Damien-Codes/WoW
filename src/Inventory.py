# import
import random

class Inventory:
    def __init__(self, name, weight):
        self._name = name
        self._weight = weight


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
            raise ValueError (f"Error : The name must be a non-empty string.")
    @weight.setter
    def weight(self, new_weight):
        self._weight = new_weight
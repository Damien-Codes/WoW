class Weapon:
    def __init__(self, name, damage, length, weight, health):
        self._name = name
        self._damage = damage
        self._length = length
        self._weight = weight
        self._health = health

    # Getters
    @property
    def name(self):
        return self._name

    @property
    def damage(self):
        return self._damage

    @property
    def length(self):
        return self._length

    @property
    def weight(self):
        return self._weight

    @property
    def health(self):
        return self._health

    # Setters
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and len(new_name.strip()) > 0:
            self._name = new_name
        else:
            print(f"Error : The name must be a positive number !")
            self._name = "weapon unknown"

    @damage.setter
    def damage(self, new_damage):
        if isinstance(new_damage, (int, float)) and new_damage >= 0:
            self._damage = new_damage
        else:
            raise ValueError (f"Error : The damage must be a positive number !")
            self._damage = 10

    @length.setter
    def length(self, new_length):
        if isinstance(new_length, (int, float)) and new_length > 0:
            self._length = new_length
        else:
            raise ValueError(f"Error : The length must be a positive number !")
            self._length = 50

    @weight.setter
    def weight(self, new_weight):
        if isinstance(new_weight, (int, float)) and new_weight > 0:
            self._weight = new_weight
        else:
            raise ValueError(f"Error : The weight must be a positive number !")
            self._weight = 5

    @health.setter
    def health(self, new_health):
        if isinstance(new_health, (int, float)) and new_health >= 0:
            self._health = new_health
        else:
            raise ValueError(f"Error : The health must be a positive number !")
            self._health = 100
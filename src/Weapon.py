class Weapon:
    def __init__(self, name, damage, length, weight, health):
        self._name = name  # ✅ Attributs privés pour éviter la récursion
        self._damage = damage
        self._length = length
        self._weight = weight
        self._health = health

    # ✅ Getters
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

    # ✅ Setters
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and len(new_name.strip()) > 0:
            self._name = new_name  # ✅ Modifie `_name`
        else:
            print("Erreur : Le nom doit être une chaîne de caractères non vide.")
            self._name = "Arme inconnue"  # ✅ Nom par défaut

    @damage.setter
    def damage(self, new_damage):
        if isinstance(new_damage, (int, float)) and new_damage >= 0:
            self._damage = new_damage  # ✅ Modifie `_damage`
        else:
            print("Erreur : Les dégâts doivent être un nombre positif.")
            self._damage = 10  # ✅ Valeur par défaut

    @length.setter
    def length(self, new_length):
        if isinstance(new_length, (int, float)) and new_length > 0:
            self._length = new_length  # ✅ Modifie `_length`
        else:
            print("Erreur : La longueur doit être un nombre positif.")
            self._length = 50  # ✅ Valeur par défaut

    @weight.setter
    def weight(self, new_weight):
        if isinstance(new_weight, (int, float)) and new_weight > 0:
            self._weight = new_weight  # ✅ Modifie `_weight`
        else:
            print("Erreur : Le poids doit être un nombre positif.")
            self._weight = 5  # ✅ Valeur par défaut

    @health.setter
    def health(self, new_health):
        if isinstance(new_health, (int, float)) and new_health >= 0:
            self._health = new_health  # ✅ Modifie `_health`
        else:
            print("Erreur : La durabilité doit être un nombre positif.")
            self._health = 100  # ✅ Valeur par défaut
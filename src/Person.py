# import

class Person:
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
            print("Erreur : Le nom doit être une chaîne de caractères non vide.")

    @health.setter
    def health(self, new_health):
        if new_health >= 0:
            self._health = new_health
        else:
            print("Vous êtes mort !!")
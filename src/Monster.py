# import class
import random
from Person import Person


class Monster(Person):
    def __init__(self, name, health):
        super().__init__(name, health)


    # attack monster
    @staticmethod
    def attack_monster(target):
        damage = random.randint(5, 10)
        target.health = target.health - damage
        return damage

    # Création de monster
def create_monster():
    print("Création de votre monstre ╬")
    name = input("Création du nom de votre monstre : ")
    health = random.randint(80, 100)
    monster1 = Monster(name, health)
    print("Votre monstre s'appelle désormais", monster1.name + " avec une vie de ", str(monster1.health) + " pv !")
    return monster1
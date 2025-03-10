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
    
    
    def fight(hero, monster):
        # random attacker
        attacker = Character.first_attack(hero, monster)
        print(f"{attacker.name} attacks first !")

        if attacker == hero:
            while True:
                # attack hero
                damage_hero = hero.attack(monster)
                print(f"{hero.name} inflicts  {damage_hero} damage at {monster.name}.")

                if not monster.isAlive():
                    break

                # Le monstre attaque
                damage_monster = monster.attack(hero)
                print(f"{monster.name} inflicts {damage_monster} damage at {hero.name}.")

                if not hero.isAlive():
                    break
        else:
            while True:
                # Le monstre attaque
                damage_monster = monster.attack(hero)
                print(f"{monster.name} inflicts {damage_monster} damage at {hero.name}.")

                if not hero.isAlive():
                    break

                # Le héros attaque
                damage_hero = hero.attack(monster)
                print(f"{hero.name} inflicts {damage_hero} damage at {monster.name}.")

                if not monster.isAlive():
                    break

        if monster.isAlive():
            print(f"{hero.name} is dead ! 💀  {monster.name} won ! 🏆")
        if hero.isAlive():
            print(f"{monster.name} is dead ! 💀  {hero.name} won ! 🏆")


    def first_attack(hero, monster):
        attacker = random.choice([hero, monster]) # TODO chercher l'arme ds inventory
        return attacker
# import
import random

from src.stack.Inventory import Inventory


class Character:
    def __init__(self, name, health, stamina, shield, foods):
        self._name = name
        self._health = health
        self._stamina = stamina
        self._shield = shield
        self._foods = foods
        self._weapon = None
        self.inventory_Items = [self.weapon, shield, foods]
        self.Inventory = Inventory(name="Inventory of " + name, weight=10)

    # Getters
    @property
    def name(self):
        return self._name
    @property
    def health(self):
        return self._health
    @property
    def stamina(self):
        return self._stamina
    @property
    def shield(self):
        return self._shield
    @property
    def foods(self):
        return self._foods
    @property
    def weapon(self):
        return self._weapon

    # Setters
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and len(new_name) > 0:
            self._name = new_name
        else:
            raise ValueError("Error : The name must be a non-empty string.")
    @health.setter
    def health(self, new_health):
        self._health = new_health
    @weapon.setter
    def weapon(self, new_weapon):
        self._weapon = new_weapon
    @stamina.setter
    def stamina(self, new_stamina):
        if isinstance(new_stamina, (int, float)) and new_stamina >= 0:
            self._stamina = new_stamina
        else:
            raise ValueError("Stamina must be a positive number.")
    @shield.setter
    def shield(self, new_shield):
        self._shield = new_shield
    @foods.setter
    def foods(self, new_foods):
        self._foods = new_foods
    def attack(self, target):
        if self.Inventory.weapon:
            damage = random.randint(25, 30)
            target.health = target.health - damage
            return damage
        else:
            print(f"{self.name} has no weapon for attacking.")
            return 0
        
    # method
    def isAlive(self):
        return self.health > 0

    def fight(hero, monster):
        attacker = Character.first_attack(hero, monster)
        print(f"{attacker.name} attacks first !")

        if attacker == hero:
            while True:
                damage_hero = hero.attack(monster)
                print(f"{hero.name} inflicts {damage_hero} damage on {monster.name}.")
                if not monster.isAlive():
                    break
                damage_monster = monster.attack(hero)
                print(f"{monster.name} inflicts {damage_monster} damage on {hero.name}.")
                if not hero.isAlive():
                    break
        else:
            while True:
                damage_monster = monster.attack(hero)
                print(f"{monster.name} inflicts {damage_monster} damage on {hero.name}.")
                if not hero.isAlive():
                    break
                damage_hero = hero.attack(monster)
                print(f"{hero.name} inflicts {damage_hero} damage on {monster.name}.")
                if not monster.isAlive():
                    break

        if monster.isAlive():
            print(f"{hero.name} is dead! 💀 {monster.name} won! 🏆")
        if hero.isAlive():
            print(f"{monster.name} is dead! 💀 {hero.name} won! 🏆")

    def first_attack(hero, monster):
        return random.choice([hero, monster])
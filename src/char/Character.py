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

        self.inventory = Inventory(name="Inventory of " + name, weight=10)

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
            raise ValueError("Name must be a non-empty string.")

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
        if self.inventory.weapon:
            return self.inventory.weapon.damage
        else:
            print(f"{self.name} has no weapon. Attacking with fists.")
            return 5  # basic damage

    def isAlive(self):
        return self.health > 0

    @staticmethod
    def fight(hero, monster):
        attacker = Character.first_attack(hero, monster)
        defender = monster if attacker == hero else hero
        print(f"{attacker.name} aattack first !\n")

        # First round whithout defender
        weapon = attacker.inventory.weapon
        base_damage = weapon.damage if weapon else 5
        attacker.stamina = max(attacker.stamina - 5, 0)
        defender.health -= base_damage
        print(f"{attacker.name} attack with {weapon.name if weapon else 'this HP'} and inflict {base_damage} damage at {defender.name}.")

        if not defender.isAlive():
            print(f"\n{defender.name} is dead ! 💀")
            print(f"\n🏆 {attacker.name} won !")
            return

        # round to round
        while hero.isAlive() and monster.isAlive():
            for attacker_p, defender_p in [(defender, attacker), (attacker, defender)]:
                if not attacker_p.isAlive() or not defender_p.isAlive():
                    break

                # if draw stop fight
                if (
                        hero.stamina <= 0 and not hero.inventory.foods and
                        monster.stamina <= 0 and not monster.inventory.foods
                ):
                    print("\n⚠️ Both fighters are exhausted and out of food.")
                    print("💤 The fight stops. Match drawn.")
                    return

                # random action choice
                action = random.choice(["attack", "defend", "eat"])

                # Eat if possible
                if action == "eat":
                    if attacker_p.inventory.foods:
                        food = attacker_p.inventory.foods.pop(0)
                        attacker_p.stamina += food.stamina_gain
                        print(f"{attacker_p.name} chooses to eat {food.name} 🍽️ (+{food.stamina_gain} stamina).")
                        continue
                    else:
                        print(f"{attacker_p.name} wanted to eat but ran out of food.")

                # Defend yourself (lose a shield without taking damage)
                if action == "defend":
                    if attacker_p.inventory.shields:
                        shield = attacker_p.inventory.shields.pop(0)
                        attacker_p.stamina = max(attacker_p.stamina - 3, 0)
                        print(f"{attacker_p.name} chooses to defend itself with {shield.name} 🛡️. The shield is destroyed.")
                        continue
                    else:
                        print(f"{attacker_p.name} wanted to defend himself but no longer had a shield.")

                # 🗡️ Attack
                weapon = attacker_p.inventory.weapon
                base_damage = weapon.damage if weapon else 5

                if defender_p.inventory.shields:
                    shield = defender_p.inventory.shields.pop(0)
                    reduced_damage = max(base_damage - shield.damageabsorption, 0)
                    print(f"{defender_p.name} blocked with {shield.name}, "
                          f"reduced the damage to {reduced_damage}. The shield is destroyed.")
                else:
                    reduced_damage = base_damage

                attacker_p.stamina = max(attacker_p.stamina - 5, 0)
                defender_p.health -= reduced_damage
                print(f"{attacker_p.name} attack with {weapon.name if weapon else 'their hands'} "
                      f"and inflicts {reduced_damage} damage to {defender_p.name}.")

                if not defender_p.isAlive():
                    print(f"\n{defender_p.name} is dead ! 💀")
                    break

        # End
        if hero.isAlive():
            print(f"\n🏆 {hero.name} won !")
        else:
            print(f"\n🏆 {monster.name} won !")



    @staticmethod
    def first_attack(hero, monster):
        return random.choice([hero, monster])

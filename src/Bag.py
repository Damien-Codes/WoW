class Bag:
    def __init__(self):
        self._weapon = None
        self._shields = []
        self._foods = []

    # Getters
    @property
    def weapon(self):
        return self._weapon
    @property
    def shields(self):
        return self._shields
    @property
    def foods(self):
        return self._foods

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
            f"🛡️ Shields : {shield_list}\n"
            f"🍏 Foods : {food_list}"
        )
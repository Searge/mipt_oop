# Abstract Factory
# Практическая реализация паттерна


class HeroFactory:
    class Hero:
        def __init__(self, name):
            self.name = name

    class Spell:
        pass

    class Weapon:
        pass

    @classmethod
    def create_hero(cls, name):
        return cls.Hero(name)

    @classmethod
    def create_spell(cls):
        return cls.Spell()

    @classmethod
    def create_weapon(cls):
        return cls.Weapon()


class WarriorFactory(HeroFactory):
    class Hero:
        def __init__(self, name):
            self.name = name
            self.spell = None
            self.weapon = None

        def add_spell(self, spell):
            self.spell = spell

        def add_weapon(self, weapon):
            self.weapon = weapon

        def hit(self):
            print(f"Warrior {self.name} hits with {self.weapon.hit()}")

        def cast(self):
            print(f"Warrior {self.name} hits with {self.spell.cast()}")

    class Weapon:
        def hit(self):
            return "Claymore"

    class Spell:
        def cast(self):
            return "Power"


class MageFactory(HeroFactory):
    class Hero:
        def __init__(self, name):
            self.name = name
            self.weapon = None
            self.armor = None
            self.spell = None

        def add_weapon(self, weapon):
            self.weapon = weapon

        def add_spell(self, spell):
            self.spell = spell

        def hit(self):
            print(f"Mage {self.name} uses {self.weapon.hit()}")
            self.weapon.hit()

        def cast(self):
            print(f"Mage {self.name} casts {self.spell.cast()}")
            self.spell.cast()

    class Weapon:
        def hit(self):
            return "Staff"

    class Spell:
        def cast(self):
            return "Fireball"


class AssassinFactory(HeroFactory):
    class Hero:
        def __init__(self, name):
            self.name = name
            self.spell = None
            self.weapon = None
            self.armor = None

        def add_spell(self, spell):
            self.spell = spell

        def add_weapon(self, weapon):
            self.weapon = weapon

        def hit(self):
            print(f"Assassin {self.name} uses {self.weapon.hit()}")

        def cast(self):
            print(f"Assassin {self.name} cast {self.spell.cast()}")

    class Weapon:
        def hit(self):
            return "Dagger"

    class Spell:
        def cast(self):
            return "Invisibility"


def create_hero(factory):
    hero = factory.create_hero("Nagibator")
    weapon = factory.create_weapon()
    spell = factory.create_spell()

    hero.add_weapon(weapon)
    hero.add_spell(spell)

    return hero


if __name__ == "__main__":
    factory = MageFactory()
    player = create_hero(factory)
    player.cast()
    player.hit()

    factory = AssassinFactory()
    player = create_hero(factory)
    player.cast()
    player.hit()

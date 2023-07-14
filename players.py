import random

from player_skills import get_player_attack_modifiers, get_player_defence_modifiers


class HeroPropertyException(ValueError):
    pass


class Field:

    def __set_name__(self, owner, name):
        self.private_name = '_' + name

    def __init__(self, min_value=None, max_value=None):
        self.min_value = min_value
        self.max_value = max_value

    def __set__(self, obj, value):
        if not getattr(obj, 'summoned', None):
            self.validate(value)
        setattr(obj, self.private_name, value)

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private_name)

    def validate(self, value):
        if not self.min_value <= value <= self.max_value:
            raise HeroPropertyException(f'Provided Value: {value} must be between {self.min_value} - {self.max_value}')


class Player:
    def __init__(self, health, strength, defence, speed, luck):
        self.health = health
        self.strength = strength
        self.defence = defence
        self.speed = speed
        self.luck = luck
        self.summoned = True
        self.skills = {}

    def __gt__(self, other):
        if self.speed > other.speed:
            return True
        elif self.speed < other.speed:
            return False
        else:
            if self.luck > other.luck:
                return True
            elif self.luck < other.luck:
                return False
        return False

    def is_healthy(self):
        return self.health > 0

    def take_damage(self, other):
        damage = other.strength - self.defence
        if random.randint(0, 100) < self.luck:
            print(f"{self} got lucky and dodged {damage} damage")
            return

        attack_modifiers = get_player_attack_modifiers(other)
        if attack_modifiers:
            for modifier in attack_modifiers:
                damage = modifier(damage)

        defence_modifiers = get_player_defence_modifiers(self)
        if defence_modifiers:
            for modifier in defence_modifiers:
                damage = modifier(damage)

        self.health -= damage
        print(f"{self} got hit for {damage} damage, health remaining {self.health if self.health > 0 else 0}")

    def register_skill(self, name, func):
        self.skills["skill_" + name] = func


class Hero(Player):
    health = Field(min_value=70, max_value=100)
    strength = Field(min_value=70, max_value=80)
    defence = Field(min_value=45, max_value=55)
    speed = Field(min_value=40, max_value=50)
    luck = Field(min_value=10, max_value=30)

    def __str__(self):
        return "<Noble Hero>"


class Villain(Player):
    health = Field(min_value=60, max_value=90)
    strength = Field(min_value=60, max_value=90)
    defence = Field(min_value=40, max_value=60)
    speed = Field(min_value=40, max_value=60)
    luck = Field(min_value=25, max_value=40)

    def __str__(self):
        return "<Bad Villain>"

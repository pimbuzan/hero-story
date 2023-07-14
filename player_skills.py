import random
from abc import abstractmethod, ABC


class Modifier:
    ATTACK = "ATTACK"
    DEFENCE = "DEFENCE"


class Skill(ABC):
    def __init__(self, chance):
        self.chance = chance

    @abstractmethod
    def __call__(self, *args, **kwargs):
        pass


class CriticalStrike(Skill):
    NAME = "Critical Strike"
    MODIFIER = Modifier.ATTACK

    def __call__(self, damage, *args, **kwargs):
        critical_damage = damage
        if random.randint(0, 100) < self.chance:
            critical_damage = damage * 2
            print(f"Attacker has used {self.NAME} x2")
            if random.randint(0, 100) < 1:
                critical_damage = damage * 3
                print(f"Attacker has used {self.NAME} x3")
        return critical_damage


class Resilience(Skill):
    NAME = "Resilience"
    MODIFIER = Modifier.DEFENCE

    def __init__(self, activated, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.activated = activated

    def __call__(self, damage, *args, **kwargs):
        if self.activated:
            self.activated = False
            return damage
        if random.randint(0, 100) < self.chance:
            print(f"Defender has used {self.NAME}")
            self.activated = True
            damage = damage / 2
        return damage


def get_player_skills(player):
    skill_list = []
    if hasattr(player, 'skills'):
        for k, v in player.skills.items():
            if k.startswith("skill") and callable(v):
                skill_list.append(v)
    return skill_list


def get_player_attack_modifiers(player):
    return filter(lambda skill: skill.MODIFIER == Modifier.ATTACK, get_player_skills(player))


def get_player_defence_modifiers(player):
    return filter(lambda skill: skill.MODIFIER == Modifier.DEFENCE, get_player_skills(player))
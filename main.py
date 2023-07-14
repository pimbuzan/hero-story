import random

from player_skills import CriticalStrike, Resilience
from players import Hero, Villain
from game import Game


def make_hero(*hero_attrs):
    hero = Hero(*hero_attrs)
    hero.register_skill("critical_strike", CriticalStrike(chance=10))
    hero.register_skill("resilience", Resilience(chance=20, activated=False))
    return hero


def main():
    hero_attrs = (
        random.randint(70, 100),
        random.randint(70, 80),
        random.randint(45, 55),
        random.randint(40, 50),
        random.randint(10, 30),
    )
    hero_attrs2 = (
        random.randint(70, 100),
        random.randint(70, 80),
        random.randint(45, 55),
        random.randint(40, 50),
        random.randint(10, 30),
    )
    villain_attrs = (
        random.randint(60, 90),
        random.randint(60, 90),
        random.randint(40, 60),
        random.randint(40, 60),
        random.randint(25, 40),
    )
    hero1, hero2 = make_hero(*hero_attrs), make_hero(*hero_attrs2)
    import ipdb; ipdb.set_trace()
    game = Game(make_hero(*hero_attrs), Villain(*villain_attrs))
    game.end_game()


if __name__ == '__main__':
    main()

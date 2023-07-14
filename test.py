import pytest
from unittest.mock import patch

from game import Game
from player_skills import CriticalStrike, Resilience
from players import Hero, HeroPropertyException, Villain


@pytest.mark.parametrize('properties, success', [
    # health, strength, defence, speed, luck
    ((70, 70, 45, 40, 10), True),
    ((69, 70, 45, 40, 10), False),
    ((70, 81, 45, 40, 10), False)
])
def test_hero_init(properties, success):
    if success:
        Hero(*properties)
    else:
        with pytest.raises(HeroPropertyException):
            Hero(*properties)


def test_hero_attr():
    new_hero = Hero(70, 70, 45, 40, 10)
    assert new_hero.health == 70
    assert new_hero.strength == 70
    assert new_hero.defence == 45
    assert new_hero.speed == 40
    assert new_hero.luck == 10


@pytest.mark.parametrize('hero_attr, villain_atrr, winner', [
    # health, strength, defence, speed, luck
    ((70, 70, 45, 40, 10), (60, 60, 40, 40, 25), Villain),
    ((70, 70, 45, 50, 10), (60, 60, 40, 40, 25), Hero),
    # TODO BUG: not specified if both player have the same speed & luck
    # ((70, 70, 45, 40, 25), (60, 60, 40, 40, 25), Hero),
])
def test_faster_player(hero_attr, villain_atrr, winner):
    hero = Hero(*hero_attr)
    villain = Villain(*villain_atrr)
    if issubclass(winner, Hero):
        assert hero > villain
    else:
        assert villain > hero


def test_gameplay_player_switch_roles():
    hero = Hero(70, 70, 45, 40, 10)
    villain = Villain(60, 60, 40, 40, 25)
    game = Game(hero, villain)
    assert villain, hero in game.get_first_striker()
    assert hero, villain in game.get_next_striker()


@patch('players.random')
def test_gameplay_player_luck_no_damage(mock_random):
    mock_random.randint.return_value = 0
    hero = Hero(70, 70, 45, 40, 10)
    villain = Villain(60, 60, 40, 40, 25)
    game = Game(hero, villain)
    game.play_round()
    assert hero.health == 70


@patch('players.random')
def test_gameplay_player_no_luck_damage(mock_random):
    mock_random.randint.return_value = 100
    hero = Hero(70, 70, 45, 40, 10)
    villain = Villain(60, 60, 40, 40, 25)
    game = Game(hero, villain)
    game.play_round()
    assert hero.health == 55


@patch('players.random')
def test_end_game_on_player_death(mock_random):
    mock_random.randint.return_value = 100
    hero = Hero(70, 70, 45, 40, 10)
    villain = Villain(60, 60, 40, 40, 25)
    game = Game(hero, villain)
    game.end_game()
    assert game.rounds == 5


@patch('players.random')
def test_end_game_on_max_rounds(mock_random):
    mock_random.randint.return_value = 0
    hero = Hero(70, 70, 45, 40, 10)
    villain = Villain(60, 60, 40, 40, 25)
    game = Game(hero, villain)
    game.end_game()
    assert game.rounds == 20


@patch('player_skills.random')
@patch('players.random')
def test_player_critical_strike_3x(mock_luck, mock_skill_chance):
    mock_luck.randint.return_value = 100
    mock_skill_chance.randint.side_effect = [0, 0]
    hero = Hero(70, 70, 45, 40, 10)
    hero.register_skill("critical_strike", CriticalStrike(chance=10))
    villain = Villain(60, 60, 40, 40, 25)
    villain.take_damage(hero)
    assert villain.is_healthy() is False
    assert villain.health == -30


@patch('player_skills.random')
@patch('players.random')
def test_player_critical_strike_2x(mock_luck, mock_skill_chance):
    mock_luck.randint.return_value = 100
    mock_skill_chance.randint.side_effect = [0, 1]
    hero = Hero(70, 70, 45, 40, 10)
    hero.register_skill("critical_strike", CriticalStrike(chance=10))
    villain = Villain(60, 60, 40, 40, 25)
    villain.take_damage(hero)
    assert villain.is_healthy() is False
    assert villain.health == 0


@patch('player_skills.random')
@patch('players.random')
def test_player_resilience_skill(mock_luck, mock_skill_chance):
    mock_luck.randint.return_value = 100
    mock_skill_chance.randint.return_value = 0
    hero = Hero(70, 70, 45, 40, 10)
    hero.register_skill("resilience", Resilience(chance=20, activated=False))
    villain = Villain(60, 60, 40, 40, 25)
    hero.take_damage(villain)
    assert hero.health == 70 - (15/2)
    remaining_health = hero.health
    hero.take_damage(villain)
    assert hero.health == remaining_health - 15

from collections import defaultdict


def announce_winner(game_round, winner, looser):
    print(f"Game ended:::{game_round}")
    print(f"{looser} got slayed!")
    print(f"{winner} is the winner")


class Game:
    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        self.rounds = 1
        self.status = {'rounds': defaultdict(dict)}

    def end_game(self):
        while self.rounds < 20:
            if not self.player_1.is_healthy():
                announce_winner(self.rounds, self.player_2, self.player_1)
                break
            if not self.player_2.is_healthy():
                announce_winner(self.rounds, self.player_1, self.player_2)
                break
            self.play_round()

    def play_round(self):
        if self.rounds == 1:
            attacker, defender = self.get_first_striker()
            print("Game is starting:::Round 1")
            print(f"First to strike is {attacker}")
        else:
            attacker, defender = self.get_next_striker()
            print(f"Game round:::{self.rounds}")
            print(f"Next to strike is {attacker}")
        self.attack(attacker, defender)

    def get_first_striker(self):
        if self.player_1 > self.player_2:
            return self.player_1, self.player_2
        return self.player_2, self.player_1

    def attack(self, attacker, defender):
        self.status['rounds'][self.rounds]['attacker'] = attacker
        self.status['rounds'][self.rounds]['defender'] = defender
        self.rounds += 1
        defender.take_damage(attacker)

    def get_next_striker(self):
        return (self.status['rounds'][self.rounds-1]['defender'],
                self.status['rounds'][self.rounds-1]['attacker'])


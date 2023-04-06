from brain_games.games.brain_gcd import gcd_game
from brain_games.games.logic import greet, congrats


def main():
    name = greet()
    counter = 0
    gcd_game(name)
    congrats(name, counter)	


if __name__ == '__main__':
    main()

from brain_games.games.brain_even import even_game
from brain_games.games.logic import greet, congrats


def main():
    name = greet()
    counter = 0
    even_game(name)
    congrats(name)


if __name__ == '__main__':
    main()

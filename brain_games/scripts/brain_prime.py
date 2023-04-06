from brain_games.games.brain_prime import prime_game
from brain_games.games.logic import greet, congrats


def main():
    name = greet()
    prime_game(name)


if __name__ == '__main__':
    main()

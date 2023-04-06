from brain_games.games.brain_progression import progression_game
from brain_games.games.logic import greet, congrats


def main():
    name = greet()
    counter = 0
    progression_game(name)
    congrats(name, counter)	


if __name__ == '__main__':
    main()

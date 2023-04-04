from brain_games.games.brain_calc import calculator_game
from brain_games.games.logic import greet, congrats


def main():
    name = greet()
    calculator_game(name)
    congrats(name)	


if __name__ == '__main__':
    main()

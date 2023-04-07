from brain_games.games.brain_calc import calculator_game
from brain_games.games.logic import logic


def main():
    name = greet()
    counter = 0
    calculator_game(name)
    congrats(name, counter)


if __name__ == '__main__':
    main()

import random
import math
from brain_games.games.logic import congrats


def generate_question():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    question = f"{number1} {number2}"
    return number1, number2, question


def calculate_answer(number1, number2):
    return math.gcd(number1, number2)


def gcd_game(name):
    counter = 0
    while counter < 3:
        number1, number2, question = generate_question()
        print('Find the greatest common divisor of given numbers.')
        print(f'Question: {question}')
        correct_answer = calculate_answer(number1, number2)
        user_answer = input('Your answer: ')
        if int(user_answer) == correct_answer and user_answer.isdigit():
            print('Correct!')
            counter += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            break
    print(congrats(name, counter))


if __name__ == '__main__':
    main()

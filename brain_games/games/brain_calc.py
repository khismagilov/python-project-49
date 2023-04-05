import random
from brain_games.games.logic import greet, congrats


def generate_question():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    operations = ['+', '-', '*']
    operation = random.choice(operations)
    question = f"{number1} {operation} {number2}"
    print('What is the result of the expression?')
    print(f'Question: {question}')


def calculator_game(name):
    counter = 0
    while counter < 3:
        asked_question = generate_question()
        user_answer = input('Your answer: ')
        if operation == '+':
            answer = number1 + number2
        elif operation == '-':
            answer = number1 - number2
        else:
            answer = number1 * number2

        if int(user_answer) == answer:
            print('Correct!')
            counter += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{answer}'.")
            break
    print(congrats(name))

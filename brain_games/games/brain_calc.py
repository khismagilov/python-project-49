import random
from brain_games.games.logic import congrats


def generate_question():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    operations = ['+', '-', '*']
    operation = random.choice(operations)
    question = f"{number1} {operation} {number2}"
    answer = calculate_answer(number1, number2, operation)
    return question, answer


def calculate_answer(num1, num2, op):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2


def calculator_game(name):
    print('What is the result of the expression?')
    counter = 0
    while counter < 3:
        question, correct_answer = generate_question()
        user_answer = input(f'Question: {question}\nYour answer: ')
        if int(user_answer) == correct_answer:
            print('Correct!')
            counter += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            break
    print(congrats(name, counter))

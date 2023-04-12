import random


RULES = 'What is the result of the expression?'


def get_question():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    operations = ['+', '-', '*']
    operation = random.choice(operations)
    question = f"{number1} {operation} {number2}"
    return question, correct_answer


def get_answer():
    if operation == '+':
        correct_answer = str(number1 + number2)
    elif operation == '-':
        correct_answer = str(number1 - number2)
    elif operation == '*':
        correct_answer = str(number1 * number2)
    return correct_answer

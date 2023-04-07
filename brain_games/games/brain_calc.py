import random


RULES = 'What is the result of the expression?'


def generate_question_and_answer():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    operations = ['+', '-', '*']
    operation = random.choice(operations)
    question = f"{number1} {operation} {number2}"
    if operation == '+':
        correct_answer = num1 + num2
    elif operation == '-':
        correct_answer = num1 - num2
    elif operation == '*':
        correct_answer = num1 * num2
    return question, correct_answer

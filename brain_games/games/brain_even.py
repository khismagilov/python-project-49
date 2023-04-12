import random


RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_game():
    question = random.randint(1, 100)
    if question % 2 == 0:
        correct_answer = 'yes'
    if question % 2 == 1:
        correct_answer = 'no'
    return question, correct_answer

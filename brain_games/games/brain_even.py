import random


RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_right_answer():
    question = random.randint(1, 100)
    if question % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer

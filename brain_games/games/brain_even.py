import random


RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_right_answer():
    number = random.randint(1, 100)
    print(f'Question: {number}')
    correct_answer = 'yes' if number % 2 == 0 else 'no'
    if answer.lower() == 'yes':
        return number % 2 == 0
    elif answer.lower() == 'no':
        return number % 2 != 0
    else:
        return False

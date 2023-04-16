import random


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(question):
    return all(question % i != 0 for i in range(2, int(question ** 0.5) + 1))


def get_question_and_right_answer():
    question = random.randint(1, 100)
    correct_answer = 'yes' if is_prime(question) and question > 1 else 'no'
    return question, correct_answer

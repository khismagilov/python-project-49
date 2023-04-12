import random
import math


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_and_right_answer():
    question = random.randint(1, 100)
    is_prime = all(question % i != 0 for i in range(2, math.isqrt(question) + 1))
    correct_answer = 'yes' if is_prime and question > 1 else 'no'
    return question, correct_answer

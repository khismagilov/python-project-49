import random
import math


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question():
    n = random.randint(1, 100)
    question = n
    is_prime = all(n % i != 0 for i in range(2, math.isqrt(n) + 1))
    is_prime = is_prime and n > 1
    correct_answer = 'yes' if is_prime else 'no'
    return question, correct_answer

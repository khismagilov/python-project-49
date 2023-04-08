import random
import math


def get_question_and_right_answer():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    question = f"{number1} {number2}"
    correct_answer = math.gcd(number1, number2)
    return question, correct_answer

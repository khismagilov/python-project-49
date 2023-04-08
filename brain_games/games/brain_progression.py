import random


RULES = 'What number is missing in the progression?'


def get_question_and_right_answer():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    number3 = random.randint(1, 100)
    number_list = list(range(1, 100))
    question = number_list[number1:number2:number3]
    if len(question) >= 5 and len(question) <= 10:
        random_number = random.randint(0, len(question) - 1)
        correct_answer = question[random_number]
        question[random_number] = '..'
        str_question = ' '.join([str(num) for num in question])
        return question, correct_answer
    else:
        return get_question_and_right_answer()

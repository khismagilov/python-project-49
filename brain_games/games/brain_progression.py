import random


RULES = 'What number is missing in the progression?'


def get_question_and_right_answer():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    number3 = random.randint(1, 100)
    number_list = list(range(1, 100))
    question1 = number_list[number1:number2:number3]
    if len(question1) >= 5 and len(question1) <= 10:
        random_number = random.randint(0, len(question1) - 1)
        correct_answer = str(question1[random_number])
        question1[random_number] = '..'
        question = ' '.join([str(num) for num in question1])
        return question, correct_answer
    else:
        return get_question_and_right_answer()

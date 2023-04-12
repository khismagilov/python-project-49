import random


RULES = 'What number is missing in the progression?'


def get_question():
    slice_start = random.randint(1, 100)
    slice_end = random.randint(1, 100)
    slice_step = random.randint(1, 100)
    number_list = list(range(1, 100))
    question = number_list[slice_start:slice_end:slice_step]
    correct_answer = get_answer(question)
    return question, correct_answer


def get_answer(question):
    if len(question) >= 5 and len(question) <= 10:
        random_number = random.randint(0, len(question) - 1)
        correct_answer = str(question[random_number])
        question[random_number] = '..'
        question = ' '.join([str(num) for num in question])
        return question, correct_answer
    else:
        return get_question()

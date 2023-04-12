import random


RULES = 'What number is missing in the progression?'


def get_question():
    slice_start = random.randint(1, 90)
    slice_end = random.randint(slice_start + 5, 100)
    slice_step = random.randint(1, 10)
    number_list = list(range(100))
    question = number_list[slice_start:slice_end:slice_step]
    if len(question) >= 5 and len(question) <= 10:
        return question
    else:
        return get_question()


def get_game():
    question = get_question()
    random_number = random.randint(0, len(question) - 1)
    correct_answer = str(question[random_number])
    question[random_number] = '..'
    question = ' '.join([str(num) for num in question])
    return correct_answer, question

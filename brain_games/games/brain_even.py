import random
from brain_games.games.logic import congrats


def ask_question():
    number = random.randint(1, 100)
    print(f'Question: {number}')
    return number


def is_answer_correct(number, answer):
    if answer.lower() == 'yes':
        return number % 2 == 0
    elif answer.lower() == 'no':
        return number % 2 != 0
    else:
        return False


def print_answer_result(is_correct, number, answer):
    if is_correct:
        print('Correct!')
    else:
        correct_answer = 'yes' if number % 2 == 0 else 'no'
        print(f"'{answer}' is wrong answer ;(."
              f"Correct answer was '{correct_answer}'.")


def even_game(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    counter = 0
    while counter < 3:
        correct_answer = ask_question()
        answer = input('Your answer: ')
        is_correct = is_answer_correct(correct_answer, answer)
        print_answer_result(is_correct, correct_answer, answer)
        if is_correct:
            counter += 1
        else:
            break
    print(congrats(name, counter))

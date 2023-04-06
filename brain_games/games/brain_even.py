import random
from brain_games.games.logic import greet, congrats


def ask_question():
    number = random.randint(1, 100)
    print(f'Question: {number}')
    return number


def check_answer(number, answer):
    answer_capital = answer.capitalize()
    if answer_capital == 'Yes' or answer_capital == 'No':
        if number % 2 == 0 and answer_capital == 'Yes':
            print('Correct!')
            return True
        elif number % 2 == 0 and answer_capital == 'No':
            print("'no' is wrong answer ;(. Correct answer was 'yes'")
            return False
        elif not number % 2 == 0 and answer_capital == 'No':
            print('Correct!')
            return True
        elif not number % 2 == 0 and answer_capital == 'Yes':
            print("'yes' is wrong answer ;(. Correct answer was 'no'")
            return False
    else:
        return False
    

def even_game(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    counter = 0
    while counter < 3:
        correct_answer = ask_question()
        answer = input('Your answer: ').lower()
        if check_answer(correct_answer, answer):
            print('Correct!')
            counter += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{'yes' if correct_answer % 2 == 0 else 'no'}'.")
            break
    print(congrats(name))

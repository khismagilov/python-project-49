import random
from brain_games.games.logic import congrats


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def ask_question():
    n = random.randint(1, 100)
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    print(f'Question: {n}')
    user_answer = input('Your answer: ')
    return user_answer


def prime_game(name):
    counter = 0
    while counter < 3:
        user_answer = ask_question()
        correct_answer = 'yes' if is_prime(n) else 'no'
        if user_answer.lower() == correct_answer:
            print("Correct!")
            counter += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(.' "
                  f"Correct answer was '{correct_answer}'.")
            break
    print(congrats(name, counter))

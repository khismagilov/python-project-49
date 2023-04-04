import random
from brain_games.games.logic import greet, congrats


def ask_question():
    number = random.randint(1, 100)
    print(f'Question: {number}')
    return 'yes' if number % 2 == 0 else 'no'

def play_game():
    correct_answers = 0
    while correct_answers < 3:
        correct_answer = ask_question()
        answer = prompt.string('Your answer: ').lower()
        if answer == correct_answer:
            print('Correct!')
            correct_answers += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            return False
    return True


def main():
    greet()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    if play_game():
        print(congrats(name))
    else:
        print(f"Let's try again, {name}")


if __name__ == '__main__':
    main()

import random
import prompt


def main():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print("Welcome to the Brain Games!")
    print('Answer "yes" if the number is even, otherwise answer "no".')
    correct_answers = 0
    while correct_answers < 3:
        number = random.randint(1, 100)
        print(f'Question: {number}')
        answer = input(f'Your answer: ')
        answer_capital = answer.capitalize()
        if answer_capital == 'Yes' or answer_capital == 'No':
            if number % 2 == 0 and answer_capital == 'Yes':
                print('Correct!')
                correct_answers += 1
            elif number % 2 == 0 and answer_capital == 'No':
                print("'no' is wrong answer ;(. Correct answer was 'yes'")
                break
            elif not number % 2 == 0 and answer_capital == 'Yes':
                print("'yes' is wrong answer ;(. Correct answer was 'no'")
                break
            elif not number % 2 == 0 and answer_capital == 'No':
                print('Correct!')
                correct_answers += 1
        else:
            break
    if correct_answers == 3:
        return f'Congratulations, {name}!'
    else:
        return f"Let's try again, {name}"


if __name__ == '__main__':
    main()

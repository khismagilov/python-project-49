import random
import prompt


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(calculator_game(name))


def calculator_game(name):
    correct_answers = 0
    while correct_answers < 3:
        number1 = random.randint(1, 100)
        number2 = random.randint(1, 100)
        operations = ['+', '-', '*']
        operation = random.choice(operations)
        question = f"{number1} {operation} {number2}"
        print('What is the result of the expression?')
        print(f'Question: {question}')
        user_answer = input('Your answer: ')
        if operation == '+':
            answer = number1 + number2
        elif operation == '-':
            answer = number1 - number2
        else:
            answer = number1 * number2

        if int(user_answer) == answer:
            print('Correct!')
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{answer}'.")
            break
    if correct_answers == 3:
        return f'Congratulations, {name}!'
    else:
        return f"Let's try again, {name}"


if __name__ == '__main__':
    main()

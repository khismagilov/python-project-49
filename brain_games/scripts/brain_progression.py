import random
import prompt


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    brain_progression(name)


def brain_progression(name):
    counter = 0
    while counter < 3:
        question, removed_number = generate_question()
        print(question)
        print('What number is missing in the progression?')
        user_answer = input('Your answer: ')
        if user_answer.isdigit() and int(user_answer) == int(removed_number):
            print('Correct!')
            counter += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{removed_number}'.")
            break
    if counter == 3:
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")


def generate_question():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    number3 = random.randint(1, 100)
    number_list = list(range(1, 100))
    question = number_list[number1:number2:number3]
    if len(question) >= 5 and len(question) <= 10:
        random_number = random.randint(0, len(question) - 1)
        removed_number = question[random_number]
        question[random_number] = '..'
        str_question = ' '.join([str(num) for num in question])
        return str_question, removed_number
    else:
        return generate_question()


if __name__ == '__main__':
    main()

import prompt


def greet():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def logic(game):
    name = greet()
    print(game.RULES)
    counter = 0
    while counter < 3:
        question, correct_answer = game.get_question_and_right_answer()
        user_answer = input(f'Question: {question}\nYour answer: ')
        if user_answer.lower() == correct_answer:
            print('Correct!')
            counter += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(."
                  f"Correct answer was '{correct_answer}'.")
            break
    print(congrats(name, counter))


def congrats(name, counter):
    if counter == 3:
        return f'Congratulations, {name}!'
    else:
        return f"Let's try again, {name}!"

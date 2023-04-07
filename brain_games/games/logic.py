import prompt


def greet():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def game_loop(name):
    counter = 0
    while counter < 3:
        question, correct_answer = get_question_and_right_answer()
        user_answer = input(f'Question: {question}\nYour answer: ')
        if user_answer == correct_answer:
            print('Correct!')
            counter += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(."
                  f"Correct answer was '{correct_answer}'.")
            break
    print(congrats(name, counter))


def logic(game):
    print(game.RULES)


def congrats(name, counter):
    if counter == 3:
        return f'Congratulations, {name}!'
    else:
        return f"Let's try again, {name}!"

import prompt


def greet():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def logic(game_module):
  print(game_module.RULES)
  question, right_answer = game_module.get_question_and_right_answer()


def congrats(name, counter):
    if counter == 3:
        return f'Congratulations, {name}!'
    else:
        return f"Let's try again, {name}!"

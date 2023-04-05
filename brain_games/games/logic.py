import prompt


def greet():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def congrats(name):
    if counter == 3:
        return f'Congratulations, {name}!'
    else:
        return f"Let's try again, {name}"

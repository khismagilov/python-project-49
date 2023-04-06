import prompt


def greet():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


name = greet()


def congrats(name, counter):
    if counter == 3:
        return f'Congratulations, {name}!'
    else:
        return f"Let's try again, {name}!"

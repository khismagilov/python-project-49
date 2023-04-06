import random
import prompt


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    prime_quiz(name)


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def prime_quiz(name):
    counter = 0
    while counter < 3:
        n = random.randint(1, 100)
        print('Answer "yes" if given number is prime. Otherwise answer "no".')
        print(f'Question: {n}')
        user_answer = input('Your answer: ')
        correct_answer = 'yes' if is_prime(n) else 'no'
        if user_answer.lower() == correct_answer:
            print("Correct!")
            counter += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(.' 
                  f"Correct answer was '{correct_answer}'.")
            break
    if counter == 3:
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")


if __name__ == '__main__':
    main()

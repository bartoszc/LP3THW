import random


def ask_number(question):
    response = int(input(question))
    return response


def game():
    the_number = random.randint(1, 100)
    guess = ask_number("That number is: ")
    tries = 1
    print(the_number)
    while guess != the_number:
        if guess > the_number:
            print("Too big...")
        else:
            print("Too small...")

        guess = ask_number("That number is: ")
        tries += 1

    print("You guessed! That number is", the_number)
    return tries

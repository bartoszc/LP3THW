from sys import exit
import random
import time


def gn():
    return random.randint(1, 4)

def dead(why):
    print(why, "Good job!")
    exit(0)

def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        choice = input("> ")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idead what that means.")

def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()

def gold_room():
    print("This room is full of gold. How much do you take?")

    try:
        choice = int(input("> "))
    except ValueError:
        dead("Man, learn to type a number.")

    if choice < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")

def death_room():
    time.sleep(10)
    print("This is the death room, what you excpected?")


def start():
    print("First you have to guess the number in range 1-4")
    print("Enter your guess: ")
    number = int(input('> '))
    random_number = gn()
    if number not in range(1, 5):
        dead("You dont understand the rules!")
    elif number == random_number:
        print("YOU WON!")
    else:
        if random_number == 1:
            bear_room()
        elif random_number == 2:
            cthulhu_room()
        elif random_number == 3:
            gold_room()
        else:
            death_room()

start()

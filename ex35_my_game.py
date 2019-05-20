from sys import exit
import random
import time
import gn
import hg

from hg import game
from gn import ask_number
from gn import game


def room_1():
    print('You are in the witcher room')
    print('What you gonna do?')
    witcher_trigger = False

    while True:
        choice = input("> ")

        if choice == "run":
            dead("ABRACADABRA!")
        elif choice == "stay" and not witcher_trigger:
            print("The witcher comes near to you")
            witcher_trigger = True
        elif choice == "open door" and witcher_trigger:
            room_2()
        else:
            print("I got no idead what that means.")


def room_2():
    print('You are in the romm with young couple')
    print('The man asks you - Did you slept with my wife?')

    choice = input("> ")
    if choice == 'yes':
        dead('You are so stupid')
    elif choice == 'no':
        print('You are lucky man')
        room_3()
    else:
        print("I got no idead what that means.")
        dead('That man is not so patient')


def room_3():
    print('You are in room with two kids')
    print('You have to play secret game and guess the number')
    tries = gn.game()
    print("No of tries:", tries)
    if tries in range(0, 5):
        print('You won this game but this is not the end')
        room_4()
    elif tries in range(5, 11):
        print('You go back to room1 :-(')
        room_1()
    else:
        dead('Looser')


def room_4():
    print('Last room')
    print('You have to play the hangman game')
    word, result = hg.game()
    print(f'The secret word was {word}')
    if result:
        print('YOU WON GAME!')
    else:
        dead('You was so close...')


def dead(why):
    print(why, "Good job!")
    exit(0)


def rooms_def(number):
    rooms = {1: room_1,
             2: room_2,
             3: room_3,
             4: room_4,
             }

    return rooms[number]()


def start():
    print('Welcome to the game - 4 Rooms')
    print('You will go to the iena snuroom...')
    time.sleep(5)
    room_num = random.randint(1, 4)
    print(f'number {room_num}!')
    rooms_def(room_num)


start()

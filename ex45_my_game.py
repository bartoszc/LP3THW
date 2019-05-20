from sys import exit
from random import randint
from textwrap import dedent

import time
import gn
import hg

from hg import game
from gn import ask_number
from gn import game

class Scene:

    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)


class Engine:

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last Scene
        current_scene.enter()


class Death(Scene):

    quips = ["You died.  You kinda suck at this.",
             "Your Mom would be proud...if she were smarter.",
             "Such a luser.",
             "I have a small puppy that's better at this.",
             "You're worse than your Dad's jokes."]


    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)


class room_1(Scene):

    print('You are in the witcher room')
    print('What you gonna do?')

    def enter(self):
        witcher_trigger = False

        while True:
            action = input("> ")

            if action == "run":
                return 'death'
            elif action == "stay" and not witcher_trigger:
                print("The witcher comes near to you")
                witcher_trigger = True
            elif action == "open door" and witcher_trigger:
                return 'room2'
            else:
                print("I got no idead what that means.")


class room_2(Scene):

    def enter(self):

        print('You are in the romm with young couple')
        print('The man asks you - Did you slept with my wife?')

        choice = input("> ")
        if choice == 'yes':
            return 'death'
        elif choice == 'no':
            print('You are lucky man')
            return 'room3'
        else:
            print("I got no idead what that means.")
            return 'death'


class room_3(Scene):

    def enter(self):

        print('You are in room with two kids')
        print('You have to play secret game and guess the number')

        tries = gn.game()
        print("No of tries:", tries)
        if tries in range(0, 5):
            print('You won this game but this is not the end')
            return 'room4'
        elif tries in range(5, 11):
            print('You go back to room1 :-(')
            return 'room1'
        else:
            return 'death'


class room_4(Scene):

    def enter(self):
        print('Last room')
        print('You have to play the hangman game')

        word, result = hg.game()
        print(f'The secret word was {word}')
        if result:
            print('YOU WON GAME!')
            return 'finished'
        else:
            print('You was so close...')
            return 'death'


class Finished(Scene):

    def enter(self):
        print("You won! Good job.")
        return 'finished'


class Map(object):

    scenes = {
    'room1': room_1(),
    'room2': room_2(),
    'room3': room_3(),
    'room4': room_4(),
    'death': Death(),
    'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('room1')
a_game = Engine(a_map)
a_game.play()

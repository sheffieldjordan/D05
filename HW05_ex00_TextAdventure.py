#!/usr/bin/env python3
# HW05_ex00_TextAdventure.py
##############################################################################
# Imports
from sys import exit

# Body

username = input("What's your name?")

def infinite_stairway_room(count=0):
    print(username + "walks through the door to see a dimly lit hallway.")
    print("At the end of the hallway is a", count * 'long ', 'staircase going towards some light')
    next = input("> ")
    
    # infinite stairs option
    if next == "take stairs":
        print(username + 'takes the stairs')
        if (count > 0):
            print("but " + username + " is not happy about it")
        infinite_stairway_room(count + 1)
    # option 2 == ?????

    if next == option_2:
        print(username + )
        pass


def gold_room():
    print("This room is full of gold.  How much does " + username + " take?")

    next = input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice," + username + " is not greedy, " + username + " wins!")
        exit(0)
    else:
        dead(username + " is a greedy goose!")


def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How is " + username + " going to move the bear?")
    bear_moved = False

    while True:
        next = input("> ")

        if next == "take honey":
            dead("The bear looks at " + username + " then slaps " + username + "'s face off.")
        elif next == "taunt" or "taunt bear" and not bear_moved:
            print("The bear has moved from the door. " + username + " can go through it now.")
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews " + username + "'s leg off.")
        elif next == "open" or "door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")


def cthulhu_room():
    print("Here " + username + " sees the great evil Cthulhu.")
    print("He, it, whatever stares at " + username + " and " + username + " goes insane.")
    print("Does " + username + " flee for " + username + "'s life or eat " + username + "'s head?")

    next = input("> ")

    if "flee" in next:
        main()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print("{}\n Good job!".format(why))
    exit(0)


############################################################################
def main():
    # START the TextAdventure game
    print(username + " is in a dark room.")
    print("There is a door to " + username + "'s right and left.")
    print("Which one does " + username + " take?")

    next = input("> ")

    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead(username + "stumbles around the room until" + username + "starve.")

if __name__ == '__main__':
    main()

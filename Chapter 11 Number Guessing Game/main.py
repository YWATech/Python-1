import random
import sys


def guess_number(number):

    while True:
        print("I am thinking of a number between 1 and 10, what is that number?")

        userInput = int(input(""))

        if number > userInput:
            print("Number too high")
        elif number < userInput:
            print("Number too low")
        elif number == userInput:
            print("You won")
            break


def intro():

    print("Welcome to the number guessing game, would you like to play? Press 1 for yes, press 2 for no")

    userInput = input("")

    if userInput == "1":
        number = random.randint(0,10)
        guess_number(number)

    else:
        sys.exit()


intro()
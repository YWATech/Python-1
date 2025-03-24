import time

def print_slow(str):
    for char in str:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()

def intro():
    print_slow("Welcome to the Text-based Adventure Game!")
    print_slow("You are standing in front of a mysterious castle.")
    print_slow("What will you do?")
    first_choice()

def first_choice():
    print_slow("You can either:")
    print_slow("1. Enter the castle.")
    print_slow("2. Walk away.")
    
    choice = input("Enter 1 or 2: ")
    
    if choice == '1':
        enter_castle()
    elif choice == '2':
        walk_away()
    else:
        print_slow("Invalid choice. Try again.")
        first_choice()

def enter_castle():
    print_slow("You bravely enter the castle.")
    print_slow("Inside, you find two doors. One is glowing red, the other is blue.")
    print_slow("Which door will you choose?")
    second_choice()

def second_choice():
    print_slow("1. Red Door")
    print_slow("2. Blue Door")
    
    choice = input("Enter 1 or 2: ")
    
    if choice == '1':
        red_door()
    elif choice == '2':
        blue_door()
    else:
        print_slow("Invalid choice. Try again.")
        second_choice()

def red_door():
    print_slow("You step through the red door and find yourself in a room full of treasure!")
    print_slow("Congratulations, you win!")
    play_again()

def blue_door():
    print_slow("You step through the blue door and are surrounded by darkness...")
    print_slow("You have fallen into a trap! Game Over.")
    play_again()

def walk_away():
    print_slow("You decide to walk away from the castle. Maybe next time.")
    play_again()

def play_again():
    choice = input("Do you want to play again? (yes/no): ").lower()
    
    if choice == 'yes':
        intro()
    elif choice == 'no':
        print_slow("Thanks for playing!")
    else:
        print_slow("Invalid choice. Try again.")
        play_again()

# Start the game
intro()
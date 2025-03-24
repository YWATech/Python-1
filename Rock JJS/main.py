import random

choices = ["rock", "paper", "scissors"]

def get_computer_choice():
    ##Randomly selects computers choice
    return random.choice(choices)

def get_user_choice():
    while True:
        user_choice = input('Enter rock, paper, or scissors').lower()
        if user_choice in choices:
            return user_choice
        
        else:
            print('Invalid choice, Choose again')


def determine_winnter(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Its a Tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    
    else:
        return "You lose!"
    
def play_game():
    print('Welcome to rock, paper, scissors')
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"\n you chose: {user_choice}")
    print(f"computer choice:  {computer_choice}"  )

    result = determine_winnter(user_choice, computer_choice)

    print(result)



play_game()
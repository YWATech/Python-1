import random
words = ["sarcasm", "glow", "apples", "oranges"]


hints = {
 "oranges": "Its orange",
 "apples": "its red"
}


def play_game(choice):
    guesses = 0
    max_guesses = 10
    display_word = ["_"] * len(choice)  # Start with blanks
    guessed_letters = []  # Keep track of guessed letters
    
    while guesses < max_guesses:
        print("Current word: " + " ".join(display_word))
        guess = input("Guess a letter: ").lower()
        
        # Ensure it's a single character
        if len(guess) != 1:
            print('You need to guess exactly one letter.')
            continue
        
        # Check if letter was guessed already
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        guessed_letters.append(guess)

        if guess in choice:
            print(f"Good guess! {guess} is in the word.")
            # Update display_word with correct guesses
            for i in range(len(choice)):
                if choice[i] == guess:
                    display_word[i] = guess
        else:
            print(f"Sorry, {guess} is not in the word.")
            guesses += 1

        # Check if player has won
        if "_" not in display_word:
            print(f"Congratulations! You've guessed the word: {choice}")
            break
        
        print(f"You have {max_guesses - guesses} guesses remaining.")

    if guesses == max_guesses:
        print(f"Game over! The word was: {choice}")


def choose_word(words):
    choice = random.choice(words)
    print
    play_game(choice)


def main():
    print("Would you like to play")
    userInput = input("")

    if userInput == "yes":
        choose_word(words)

if __name__ == "__main__":
    main()